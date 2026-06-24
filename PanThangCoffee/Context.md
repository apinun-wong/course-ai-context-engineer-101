# Brand Identity: Panthang Coffee

Panthang Coffee คือร้านกาแฟที่เน้นความเป็นคอมมูนิตี้และการแบ่งปัน เป็นสวรรค์ของคนรักกาแฟสไตล์รสชาติเข้มข้นที่ต้องการทางเลือกสุขภาพ ไฟล์นี้คือ Single Source of Truth สำหรับบริบททางธุรกิจของแบรนด์ Panthang Coffee ที่ AI/Agent ทุกตัวต้องอ่านและทำความเข้าใจก่อนเริ่มงานหรือตอบคำถามใดๆ เสมอ

## Core Philosophy & Concept

- เน้นเสิร์ฟ "กาแฟคั่วเข้ม" (Dark & Bold) ที่มีบอดี้หนักแน่น หอมกรุ่น ทานคู่กับนมแล้วรสชาติกาแฟไม่ดรอปและไม่ติดเปรี้ยว
- มีจุดขายหลักคือ "Milk Bar" ที่มอบอิสระให้ลูกค้าจับคู่กาแฟเข้มๆ กับ "นมทางเลือก" ที่หลากหลายที่สุดในย่านนี้

## Product Highlights (สินค้าชูโรง)

1. **Signature Coffee Beans:** เมล็ดกาแฟเบลนด์พิเศษที่ออกแบบมาเพื่อเมนูนมโดยเฉพาะ (เน้นโทน Nutty, Chocolate, Caramel)
2. **The Milk Variety (ความหลากหลายของนม):**
   - **Cow Milk (นมวัว):** นมวัวพรีเมียม หอมมันเต็มรสชาติ
   - **Oat Milk (นมโอ๊ต):** ทางเลือกยอดฮิตสำหรับสายวีแกน ให้เนื้อสัมผัสครีมมี่เข้ากับกาแฟคั่วเข้มได้ดีเยี่ยม
   - **Soy Milk (นมถั่วเหลือง):** นมทางเลือกคลาสสิก รสชาติกลมกล่อม โปรตีนสูง
   - **Almond Milk (นมอัลมอนด์):** แคลอรี่ต่ำ หอมกลิ่นถั่วคั่วบางๆ (เหมาะสำหรับคนคุมน้ำหนัก)

## Target Audience (กลุ่มลูกค้าหลัก)

- วัยทำงานและชาวคอมมูนิตี้ที่ต้องการคาเฟอีนเพื่อปลุกพลังในตอนเช้า
- ลูกค้าที่มีข้อจำกัดด้านสุขภาพ (เช่น แพ้นมวัว, ทานเจ, วีแกน) แต่อยากได้ความอร่อยแบบเต็มร้อย
- ผู้ที่หลงใหลในกาแฟนม (White Coffee) ที่รสชาติกาแฟชัดเจน ไม่ถูกนมกลบ

## Brand Tone of Voice (น้ำเสียงของแบรนด์)

- อบอุ่น เป็นกันเอง เหมือนเพื่อนที่รู้ใจ (Friendly & Welcoming)
- ใส่ใจในรายละเอียดและสุขภาพของลูกค้า (Empathetic & Caring)
- มีความเป็นมืออาชีพด้านกาแฟ (Professional)

## โครงสร้างโฟลเดอร์ (Directory Structure)

```
PanThangCoffee/
├── Context.md           # ไฟล์นี้ — บริบทหลักของแบรนด์/โปรเจกต์
├── skills/               # Skills เฉพาะทางของ Agent (โฟลเดอร์จริง — แก้ที่นี่ที่เดียว)
│   ├── template_skill.md
│   └── manager-skill/    # Persona "พี่ปั้น" ผู้จัดการร้าน (SKILL.md + references/) — ดูรายละเอียดใน Active Skills ด้านล่าง
├── .claude/skills/       # symlink → ../skills (ให้ Claude Code อ่าน skills ชุดเดียวกัน)
├── .antigravity/skills/  # symlink → ../skills (ให้ Antigravity IDE อ่าน skills ชุดเดียวกัน)
├── .agents/skills.json   # registry ชี้ไป ../skills สำหรับ agent ที่ใช้ convention นี้
├── data/                 # ข้อมูลหลังบ้าน (inventory.csv, feedback.csv, sales.csv) — ห้ามอ่านตรงๆ
├── tools/                # เครื่องมือ/การตั้งค่า Tools
├── mcp/                  # Model Context Protocol / Integration
└── script/               # Automation Scripts (เป็นทางเดียวที่เข้าถึงข้อมูลใน data/ ได้)
```

> **Skill discovery (สำคัญ):** โฟลเดอร์ `skills/` คือแหล่งจริงแห่งเดียว ส่วน `.claude/skills/` และ `.antigravity/skills/` เป็น **symlink** ชี้กลับมาที่ `../skills` เพื่อให้แต่ละ IDE มองเห็น skill เดียวกันโดยไม่ต้องทำสำเนา — เพิ่ม/แก้ skill ที่ `skills/` เท่านั้น ทุก IDE จะเห็นพร้อมกัน (clone repo บนเครื่องใหม่ให้ตั้ง `git config core.symlinks true`)

## Skills ที่ใช้งานอยู่ (Active Skills)

| Skill | ตัวละคร/Persona | หน้าที่ | Trigger |
|---|---|---|---|
| [`skills/manager-skill/SKILL.md`](skills/manager-skill/SKILL.md) | "พี่ปั้น" ผู้จัดการร้าน | วิเคราะห์ inventory และ feedback ของ Panthang Coffee สรุปสถานะสต็อก/แนวโน้มลูกค้า | "สต็อกร้านกาแฟ", "Panthang Coffee", "feedback ลูกค้า", "ช่วยเรียกพี่ปั้นมาคุยหน่อยครับ" |

เมื่อ Agent ต้องตอบคำถามเกี่ยวกับสต็อกสินค้าหรือฟีดแบคลูกค้าของ Panthang Coffee ให้ใช้ persona และกฎตาม `skills/manager-skill/SKILL.md` เป็นหลัก โดยยึด Brand Identity ในไฟล์นี้เป็นบริบทประกอบ

## กฎเกณฑ์การทำงานของ Agent (Agent Guidelines)

1. **Context-First Behavior**: ทุกครั้งที่เริ่ม Session ใหม่ หรือมีคำสั่งงานที่ต้องอิงบริบทของระบบ ให้อ่านไฟล์ `Context.md` นี้ก่อนเสมอ
2. **Skill Creation**: เมื่อต้องสร้าง Skill ใหม่ในโฟลเดอร์ `skills/` ให้คัดลอกโครงสร้างจาก `skills/template_skill.md` เป็นสารตั้งต้นเท่านั้น
3. **Consistency**: รักษาโครงสร้างโฟลเดอร์ตามที่กำหนดไว้ ห้ามเปลี่ยนแปลงโดยไม่มีเหตุผลชัดเจน
4. **Data Access Control**: ข้อมูลในโฟลเดอร์ `data/` ถือเป็นข้อมูลหลังบ้านทั้งหมด ห้ามทุก Skill อ่านไฟล์ใน `data/` ตรงๆ ต้องเรียกผ่าน script ที่กำหนด (`script/get_inventory.py`, `script/get_feedback.py`, `script/get_sales.py`) พร้อมระบุ `caller_role` ตามที่แต่ละ Skill กำหนดไว้เท่านั้น

## ผู้เกี่ยวข้อง (Stakeholders)

- _[เจ้าของร้าน Panthang Coffee / ผู้ใช้งานหลักของระบบ AI]_

## ประวัติการเปลี่ยนแปลง (Changelog)

- `2026-06-20` — สร้างโครงสร้าง Context.md เริ่มต้น
- `2026-06-20` — ปรับ Context.md เป็น Brand Identity Knowledge Base ของ Panthang Coffee
- `2026-06-20` — เพิ่มส่วน Active Skills เชื่อม `skills/ManagerSkill.md` และกฎ Data Access Control ระดับโปรเจกต์
- `2026-06-24` — อัปเดต pointer ของ Manager Skill จาก `skills/ManagerSkill.md` เป็น `skills/manager-skill/SKILL.md` (+ references/) ให้ตรงโครงสร้างไฟล์จริง
- `2026-06-24` — เพิ่ม symlink `.claude/skills/` และ `.antigravity/skills/` ชี้ไป `../skills` ให้ Claude Code และ Antigravity IDE อ่าน skills ชุดเดียวกัน + เอกสาร Skill discovery ใน Directory Structure
