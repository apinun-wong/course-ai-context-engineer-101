"""จำลองการอ่านข้อมูลยอดขายจาก database (คืนค่าเป็น JSON) แล้วแปลงเป็นข้อความให้ผู้จัดการอ่าน

เงื่อนไขการเข้าถึงข้อมูล:
- ข้อมูลถือเป็นข้อมูลหลังบ้าน (backend data) ห้าม Agent/บทบาทอื่นเปิดไฟล์ใน data/ ตรงๆ
- ต้องเรียกผ่าน get_sales_from_db() เท่านั้น และต้องระบุ caller_role="manager"
- บทบาทอื่นที่ไม่ใช่ "manager" จะถูกปฏิเสธด้วย PermissionError
"""

import csv
import json
from collections import defaultdict
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "sales.csv"
AUTHORIZED_ROLE = "manager"


def get_sales_from_db(caller_role: str) -> str:
    """จำลอง DB call: อ่านจาก sales.csv แล้วคืนค่าเป็น JSON string เหมือนได้จาก database จริง

    อนุญาตให้เรียกได้เฉพาะ caller_role == "manager" เท่านั้น
    ห้ามเปิดไฟล์ data/sales.csv ตรงๆ ไม่ว่าจะเป็น Agent หรือ Skill ใดก็ตาม
    """
    if caller_role != AUTHORIZED_ROLE:
        raise PermissionError(
            f"caller_role='{caller_role}' ไม่มีสิทธิ์ดึงข้อมูลยอดขาย "
            f"ต้องเป็น '{AUTHORIZED_ROLE}' เท่านั้น"
        )

    with open(DATA_PATH, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    for row in rows:
        row["qty_sold"] = int(row["qty_sold"])
        row["revenue"] = int(row["revenue"])

    return json.dumps(rows, ensure_ascii=False)


def format_sales_for_manager(sales_json: str) -> str:
    """แปลง JSON ยอดขายเป็นข้อความสรุปอ่านง่าย สำหรับผู้จัดการ แยกตามเดือน"""
    rows = json.loads(sales_json)

    if not rows:
        return "ยังไม่มีข้อมูลยอดขายในระบบครับ"

    by_month: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        month_key = row["date"][:7]
        by_month[month_key].append(row)

    lines = []
    for month_key in sorted(by_month):
        month_rows = by_month[month_key]
        total_qty = sum(r["qty_sold"] for r in month_rows)
        total_revenue = sum(r["revenue"] for r in month_rows)
        lines.append(f"เดือน {month_key}: ขายได้ {total_qty} ออเดอร์ ยอดขายรวม {total_revenue:,} บาทครับ")
        for row in month_rows:
            lines.append(
                f"  - {row['date']} [{row['category']}] {row['item']}: "
                f"{row['qty_sold']} แก้ว/ชิ้น = {row['revenue']:,} บาท"
            )
        lines.append("")

    return "\n".join(lines).rstrip()


if __name__ == "__main__":
    sales_json = get_sales_from_db(caller_role="manager")
    print("=== Raw JSON จาก DB (จำลอง) ===")
    print(sales_json)
    print()
    print("=== ข้อความสรุปสำหรับผู้จัดการ ===")
    print(format_sales_for_manager(sales_json))

    try:
        get_sales_from_db(caller_role="customer")
    except PermissionError as e:
        print()
        print(f"=== ทดสอบสิทธิ์: {e} ===")
