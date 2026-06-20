"""จำลองการอ่านข้อมูล feedback จาก database (คืนค่าเป็น JSON) แล้วแปลงเป็นข้อความให้ผู้จัดการอ่าน

เงื่อนไขการเข้าถึงข้อมูล:
- ข้อมูลถือเป็นข้อมูลหลังบ้าน (backend data) ห้าม Agent/บทบาทอื่นเปิดไฟล์ใน data/ ตรงๆ
- ต้องเรียกผ่าน get_feedback_from_db() เท่านั้น และต้องระบุ caller_role="manager"
- บทบาทอื่นที่ไม่ใช่ "manager" จะถูกปฏิเสธด้วย PermissionError
"""

import csv
import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "feedback.csv"
AUTHORIZED_ROLE = "manager"


def get_feedback_from_db(caller_role: str) -> str:
    """จำลอง DB call: อ่านจาก feedback.csv แล้วคืนค่าเป็น JSON string เหมือนได้จาก database จริง

    อนุญาตให้เรียกได้เฉพาะ caller_role == "manager" เท่านั้น
    ห้ามเปิดไฟล์ data/feedback.csv ตรงๆ ไม่ว่าจะเป็น Agent หรือ Skill ใดก็ตาม
    """
    if caller_role != AUTHORIZED_ROLE:
        raise PermissionError(
            f"caller_role='{caller_role}' ไม่มีสิทธิ์ดึงข้อมูล feedback "
            f"ต้องเป็น '{AUTHORIZED_ROLE}' เท่านั้น"
        )

    with open(DATA_PATH, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    for row in rows:
        row["rating"] = int(row["rating"])

    return json.dumps(rows, ensure_ascii=False)


def format_feedback_for_manager(feedback_json: str) -> str:
    """แปลง JSON feedback เป็นข้อความสรุปอ่านง่าย สำหรับผู้จัดการ"""
    rows = json.loads(feedback_json)

    if not rows:
        return "ยังไม่มีฟีดแบคจากลูกค้าในระบบครับ"

    avg_rating = sum(row["rating"] for row in rows) / len(rows)

    lines = [f"มีฟีดแบคทั้งหมด {len(rows)} รายการ คะแนนเฉลี่ย {avg_rating:.1f} ดาวครับ", ""]
    for row in rows:
        stars = "★" * row["rating"] + "☆" * (5 - row["rating"])
        lines.append(f"- {row['date']} [{stars}] {row['comment']}")

    return "\n".join(lines)


if __name__ == "__main__":
    feedback_json = get_feedback_from_db(caller_role="manager")
    print("=== Raw JSON จาก DB (จำลอง) ===")
    print(feedback_json)
    print()
    print("=== ข้อความสรุปสำหรับผู้จัดการ ===")
    print(format_feedback_for_manager(feedback_json))

    # ตัวอย่างกรณีถูกปฏิเสธสิทธิ์
    try:
        get_feedback_from_db(caller_role="customer")
    except PermissionError as e:
        print()
        print(f"=== ทดสอบสิทธิ์: {e} ===")
