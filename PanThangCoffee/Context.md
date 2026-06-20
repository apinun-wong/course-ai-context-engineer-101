# Context.md — PanThangCoffee

Single Source of Truth สำหรับบริบท เป้าหมาย และข้อกำหนดทั้งหมดของโปรเจกต์ PanThangCoffee
Agent ต้องอ่านและทำความเข้าใจไฟล์นี้ก่อนเริ่มงานหรือตอบคำถามใดๆ เสมอ

## ภาพรวมโปรเจกต์ (Overview)

- **ชื่อโปรเจกต์**: PanThangCoffee
- **สถานะ**: เริ่มต้น (Scaffold)
- **คำอธิบาย**: _[ระบุรายละเอียดโปรเจกต์ — เช่น ร้านกาแฟ/แบรนด์ PanThangCoffee ทำธุรกิจอะไร แก้ปัญหาอะไร]_

## เป้าหมาย (Goals)

- _[เป้าหมายหลักของโปรเจกต์นี้]_
- _[เป้าหมายรอง ถ้ามี]_

## ขอบเขตงาน (Scope)

- **อยู่ในขอบเขต**: _[ระบุ]_
- **ไม่อยู่ในขอบเขต**: _[ระบุ]_

## โครงสร้างโฟลเดอร์ (Directory Structure)

```
PanThangCoffee/
├── Context.md           # ไฟล์นี้ — บริบทหลักของโปรเจกต์
├── skills/               # Skills เฉพาะทางของ Agent
│   └── template_skill.md
├── tools/                # เครื่องมือ/การตั้งค่า Tools
├── mcp/                  # Model Context Protocol / Integration
└── script/               # Automation Scripts
```

## กฎเกณฑ์การทำงานของ Agent (Agent Guidelines)

1. **Context-First Behavior**: ทุกครั้งที่เริ่ม Session ใหม่ หรือมีคำสั่งงานที่ต้องอิงบริบทของระบบ ให้อ่านไฟล์ `Context.md` นี้ก่อนเสมอ
2. **Skill Creation**: เมื่อต้องสร้าง Skill ใหม่ในโฟลเดอร์ `skills/` ให้คัดลอกโครงสร้างจาก `skills/template_skill.md` เป็นสารตั้งต้นเท่านั้น
3. **Consistency**: รักษาโครงสร้างโฟลเดอร์ตามที่กำหนดไว้ ห้ามเปลี่ยนแปลงโดยไม่มีเหตุผลชัดเจน

## ข้อกำหนดทางเทคนิค (Technical Requirements)

- _[Stack/ภาษา/Framework ที่ใช้]_
- _[ข้อจำกัดด้านเทคนิค]_

## ผู้เกี่ยวข้อง (Stakeholders)

- _[เจ้าของโปรเจกต์ / ผู้ใช้งานหลัก]_

## ประวัติการเปลี่ยนแปลง (Changelog)

- `2026-06-20` — สร้างโครงสร้าง Context.md เริ่มต้น

ร้านกาแฟนี้ชื่อว่า "Nun Coffee"