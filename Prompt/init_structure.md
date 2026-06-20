# Role & Core Instruction
คุณคือ AI Assistant/Agent ที่ทำงานภายใต้โครงสร้างโปรเจกต์ที่กำหนดไว้อย่างเคร่งครัด โดยคุณจะต้องใช้ `Context.md` ที่อยู่บริเวณ Root Project เป็นแหล่งอ้างอิงหลัก (Single Source of Truth) ในการรับรู้บริบท เป้าหมาย และข้อกำหนดของโปรเจกต์นี้เสมอ ก่อนเริ่มงานหรือตอบคำถามใดๆ ให้คุณอ่านและทำความเข้าใจไฟล์ `Context.md` ก่อนทุกครั้ง

# Project Directory Structure
ให้ยึดถือและรักษารูปแบบโครงสร้างโฟลเดอร์และไฟล์ดังต่อไปนี้:

[Root Project]/
│
├── Context.md               # ไฟล์เก็บบริบทหลัก เป้าหมาย และกฎเกณฑ์ทั้งหมดของ Agent
│
├── skills/                  # โฟลเดอร์เก็บความสามารถ/กระบวนการทำงานเฉพาะทาง (Skills)
│   └── template_skill.md    # ไฟล์ Template เริ่มต้นสำหรับสร้าง Skill ใหม่ๆ
│
├── tools/                   # โฟลเดอร์เก็บเครื่องมือหรือการตั้งค่า Tools ต่างๆ
│
├── mcp/                     # โฟลเดอร์สำหรับ Model Context Protocol (MCP) หรือ Integration
│
└── script/                  # โฟลเดอร์สำหรับเก็บ Automation Scripts หรือ Executable Files

# Guideline for Agent Execution
1. **Context-First Behavior**: ทุกครั้งที่มีการเริ่มต้น Session ใหม่ หรือมีการสั่งงานที่ต้องอิงเกณฑ์ระบบ คุณจะต้องอ่านไฟล์ `Context.md` นอกสุดนี้เพื่อตรวจสอบบริบทภาพรวมเสมอ
2. **Skill Creation**: หากมีภารกิจที่ต้องสร้าง Skill ใหม่ในโฟลเดอร์ `skills/` คุณจะต้องคัดลอกรูปแบบและโครงสร้างจากไฟล์ `skills/template_skill.md` เป็นสารตั้งต้นในการพัฒนาเท่านั้น