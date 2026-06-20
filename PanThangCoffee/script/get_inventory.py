"""จำลองการอ่านข้อมูล inventory จาก database (คืนค่าเป็น JSON) แล้วแปลงเป็นข้อความให้ผู้จัดการอ่าน

เงื่อนไขการเข้าถึงข้อมูล:
- ข้อมูลถือเป็นข้อมูลหลังบ้าน (backend data) ห้าม Agent/บทบาทอื่นเปิดไฟล์ใน data/ ตรงๆ
- ต้องเรียกผ่าน get_inventory_from_db() เท่านั้น และต้องระบุ caller_role="manager"
- บทบาทอื่นที่ไม่ใช่ "manager" จะถูกปฏิเสธด้วย PermissionError
"""

import csv
import json
from datetime import date
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "inventory.csv"
AUTHORIZED_ROLE = "manager"
CRITICAL_DAYS_THRESHOLD = 3


def get_inventory_from_db(caller_role: str) -> str:
    """จำลอง DB call: อ่านจาก inventory.csv แล้วคืนค่าเป็น JSON string เหมือนได้จาก database จริง

    อนุญาตให้เรียกได้เฉพาะ caller_role == "manager" เท่านั้น
    ห้ามเปิดไฟล์ data/inventory.csv ตรงๆ ไม่ว่าจะเป็น Agent หรือ Skill ใดก็ตาม
    """
    if caller_role != AUTHORIZED_ROLE:
        raise PermissionError(
            f"caller_role='{caller_role}' ไม่มีสิทธิ์ดึงข้อมูล inventory "
            f"ต้องเป็น '{AUTHORIZED_ROLE}' เท่านั้น"
        )

    with open(DATA_PATH, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    for row in rows:
        row["stock_qty"] = int(row["stock_qty"])

    return json.dumps(rows, ensure_ascii=False)


def format_inventory_for_manager(inventory_json: str, current_date: str) -> str:
    """แปลง JSON inventory เป็นข้อความสรุปอ่านง่าย สำหรับผู้จัดการ

    current_date ใช้เป็นฐานคำนวณวันคงเหลือก่อนหมดอายุ (รูปแบบ YYYY-MM-DD)
    สินค้าที่เหลืออายุ <= CRITICAL_DAYS_THRESHOLD วัน จะถูกตีตรา "⚠️ เสี่ยงหมดอายุ (Critical)"
    """
    rows = json.loads(inventory_json)

    if not rows:
        return "ยังไม่มีข้อมูลสต็อกในระบบครับ"

    today = date.fromisoformat(current_date)
    lines = [f"มีสินค้าทั้งหมด {len(rows)} รายการในสต็อก (อ้างอิงวันที่ {current_date}) ครับ", ""]

    for row in rows:
        expiry = date.fromisoformat(row["expiry_date"])
        days_left = (expiry - today).days
        flag = " ⚠️ เสี่ยงหมดอายุ (Critical)" if days_left <= CRITICAL_DAYS_THRESHOLD else ""
        lines.append(
            f"- [{row['category']}] {row['name']}: {row['stock_qty']} {row['unit']} "
            f"(หมดอายุ {row['expiry_date']}, เหลือ {days_left} วัน){flag}"
        )

    return "\n".join(lines)


if __name__ == "__main__":
    inventory_json = get_inventory_from_db(caller_role="manager")
    print("=== Raw JSON จาก DB (จำลอง) ===")
    print(inventory_json)
    print()
    print("=== ข้อความสรุปสำหรับผู้จัดการ ===")
    print(format_inventory_for_manager(inventory_json, current_date="2026-06-20"))

    try:
        get_inventory_from_db(caller_role="customer")
    except PermissionError as e:
        print()
        print(f"=== ทดสอบสิทธิ์: {e} ===")
