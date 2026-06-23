# Best Practices: เขียน MD File สำหรับ AI Agent
### สำหรับโปรเจกต์ Software โดยเฉพาะ

> อ้างอิงจาก: Anthropic (claude.com/blog), HumanLayer Blog, Builder.io, DeployHQ Blog

---

## ข้อ 1 — เขียนให้ AI อ่าน ไม่ใช่คนอ่าน

AI ไม่มี implicit knowledge — ต้องบอกทุกอย่างที่ต้องการให้ทำ
คนอ่านเข้าใจ context ได้เอง แต่ AI ไม่มีทาง assume ได้

```markdown
❌ "ใช้ architecture ที่ดี"
✅ "Architecture: VIPER — View ห้าม business logic ทั้งหมดอยู่ใน Interactor"

❌ "เก็บ token ให้ปลอดภัย"
✅ "ห้ามเก็บ token ใน UserDefaults
    ต้องใช้ Shared/Storage/KeychainManager.swift เท่านั้น"
```

**ทดสอบ:** อ่านทุกประโยคแล้วถามว่า "AI จะเปลี่ยนพฤติกรรมได้ทันทีจากประโยคนี้ไหม?"
ถ้าไม่ใช่ → ตัดออก หรือเขียนใหม่

---

## ข้อ 2 — Actionable ทุกบรรทัด

ทุกบรรทัดต้องทำให้ AI ทำสิ่งที่ต่างออกไป
ถ้าเอาบรรทัดนั้นออกแล้ว AI ทำงานเหมือนเดิม = ไม่จำเป็น

```markdown
❌ "The app is built with modern iOS development practices."
   → AI เอาไปใช้ทำอะไรไม่ได้เลย

❌ "ระบบนี้ใช้ Clean Architecture"
   → บอกว่าอะไร แต่ไม่บอกว่าทำยังไง

✅ "ใช้ async/await ทุกที่ ห้ามใช้ completion handler ใน code ใหม่"
✅ "ทุก API call ต้องผ่าน NetworkManager.swift ห้าม call URLSession โดยตรง"
```

---

## ข้อ 3 — ห้าม vs ควร ระบุให้ชัดเจน

กฎคลุมเครือแย่กว่าไม่มีกฎ เพราะ AI จะ interpret ผิดและทำงานผิดแบบมั่นใจ
คำที่บ่งบอกว่ายังคลุมเครือ: "ดี", "เหมาะสม", "ปลอดภัย", "ควร", "เพียงพอ"

```markdown
❌ คลุมเครือ
"ควรเขียน code ที่อ่านง่าย"
"มี unit test ที่เพียงพอ"
"เก็บ token ให้ปลอดภัย"

✅ ชัดเจน
"ห้ามใช้ nested if เกิน 2 ชั้น — ใช้ guard early return แทน"
"ห้าม merge ถ้า coverage ต่ำกว่า 70% ใน Interactor layer"
"ห้ามเก็บ token ใน UserDefaults — ใช้ KeychainManager.swift"
```

**แบ่งกฎเป็น 2 ระดับในไฟล์:**
```markdown
## Hard Rules (ห้ามละเมิดเด็ดขาด)
- ห้าม import UIKit ใน Interactor
- ห้าม log token หรือ password ในทุกกรณี

## Preferences (ควรทำถ้าเป็นไปได้)
- ควรมี doc comment ทุก public function
- ควรใช้ guard early return แทน nested if
```

---

## ข้อ 4 — ระบุ Path จริง ไม่ใช่แค่ชื่อ

AI ต้องรู้ว่าไฟล์อยู่ที่ไหนจริง ๆ ชื่อคลาสอย่างเดียวไม่พอ

```markdown
❌ "ใช้ theme constants"
✅ "ดึง color จาก Shared/Theme/Colors.swift
    และ spacing จาก Shared/Theme/Spacing.swift"

❌ "มี Keychain wrapper อยู่แล้ว"
✅ "ใช้ Shared/Storage/KeychainManager.swift
    — method: save(_:forKey:), load(forKey:), delete(forKey:)"

❌ "ดู API endpoint ใน config"
✅ "API base URL อยู่ใน Config/Environment.swift
    — DEV: https://dev-api.myapp.com/v1
    — PROD: https://api.myapp.com/v1"
```

---

## ข้อ 5 — อย่าเขียนสิ่งที่ AI รู้อยู่แล้ว

General best practice ที่ AI รู้จาก training data ไม่ต้องเขียนซ้ำ
เขียนเฉพาะ project-specific knowledge เท่านั้น

```markdown
❌ ตัดออก (AI รู้อยู่แล้ว)
"ใช้ guard เพื่อ early return"
"หลีกเลี่ยง force unwrap"
"ใช้ weak self ใน closure"
"ตั้งชื่อ variable ให้สื่อความหมาย"
"VIPER ย่อมาจาก View Interactor Presenter Entity Router"
"เขียน commit message ให้ชัดเจน"

✅ เก็บไว้ (project-specific)
"RxSwift DisposeBag ต้องประกาศใน ViewController เท่านั้น ห้ามอยู่ใน Presenter"
"ชื่อ function ใน Interactor ต้องขึ้นต้นด้วย fetch, update, delete เท่านั้น"
"commit format: [TUNG-123] feat: add cart quantity"
"coverage วัดด้วย Xcode coverage report ไม่ใช่ third-party tool"
```

**ทดสอบด้วยคำถามนี้:**
> "ถ้าเปิด Swift project ใหม่เปล่า ๆ แล้วถาม AI
>  มันจะทำสิ่งนี้ถูกไหมโดยไม่ต้องบอก?"
> ถ้าใช่ → ตัดออก | ถ้าไม่ใช่ → เก็บไว้

---

## ข้อ 6 — Explain Why ไม่ใช่แค่ What

*(จาก explainx.ai และ HumanLayer Blog)*

AI ที่รู้เหตุผลจะ apply rule ได้ถูกในสถานการณ์ที่ไม่ได้คาดไว้
AI ที่รู้แค่ "อย่าทำ X" จะงงเมื่อเจอ edge case

```markdown
❌ บอกแค่ What
"ห้ามใช้ any type ใน TypeScript"

✅ บอกทั้ง What และ Why
"ห้ามใช้ any type ใน TypeScript
 เพราะมันทำลาย type safety และทำให้ refactor อันตราย
 ใช้ unknown แล้วทำ type narrowing แทน"

❌ บอกแค่ What
"ห้าม call API ใน View layer"

✅ บอกทั้ง What และ Why
"ห้าม call API ใน View layer
 เพราะ VIPER กำหนดให้ network logic อยู่ใน Interactor เท่านั้น
 ถ้า View call API โดยตรงจะทำให้ test ไม่ได้และ layer ปนกัน"
```

---

## ข้อ 7 — อย่าใส่ Code Snippet ใน MD File

*(จาก HumanLayer Blog — "Prefer pointers to copies")*

Code snippet ใน MD file จะ out-of-date เร็วมาก
และเมื่อ code จริงเปลี่ยนแต่ MD ไม่ได้อัปเดต AI จะทำตาม example เก่า

```markdown
❌ ใส่ code snippet โดยตรง
## ตัวอย่างการสร้าง Module
```swift
class HomeRouter: HomeRouterProtocol {
    weak var viewController: UIViewController?
    // ... 20 บรรทัด
}
```

✅ ชี้ไปที่ไฟล์จริงแทน
"ดูตัวอย่างการสร้าง Router ได้ที่ Modules/Home/Router/HomeRouter.swift"

✅ ถ้าจำเป็นต้องมี example ให้เก็บใน skills/ ไม่ใช่ context.md
"ดูขั้นตอนสร้าง Module ใหม่ได้ที่ .claude/skills/create-feature.md"
```

**ข้อยกเว้น:** pattern สั้น ๆ 1-3 บรรทัดที่ไม่น่าเปลี่ยน เช่น commit format หรือ naming convention ใส่ได้

---

## ข้อ 8 — แยก Responsibility ให้ถูกไฟล์

*(จาก Anthropic blog และ Builder.io)*

แต่ละไฟล์ตอบคำถามเดียว ไม่ปนกัน

```
.claude/
├── CLAUDE.md                    # "AI นี้คือใคร ทำงานยังไง"
│                                  persona, ภาษา, AI-specific rules
│                                  สั้นที่สุด — โหลดทุก session
│
├── context.md                   # "โปรเจกต์นี้คืออะไร"
│                                  tech stack, architecture, business rules
│                                  security policy, external services
│
└── skills/
    ├── review-code.md           # "วิธี review MR ทำยังไง"
    ├── create-unit-test.md      # "วิธีเขียน test ทำยังไง"
    ├── create-feature.md        # "วิธีสร้าง feature ใหม่ทำยังไง"
    └── create-merge-request.md  # "วิธีสร้าง MR ทำยังไง"
```

**กฎแบ่งง่าย ๆ:**
```
context.md = "อะไร" (what exists)
skills/    = "ยังไง" (how to do it)
CLAUDE.md  = "ใคร"  (who is the AI)
```

---

## ข้อ 9 — CLAUDE.md ควรสั้นที่สุด

*(จาก HumanLayer Blog — วิเคราะห์ Claude Code system prompt จริง)*

Claude Code มี system prompt ~50 instructions อยู่แล้ว
กิน context เกือบ 1 ใน 3 ก่อนที่คุณจะเขียนอะไรเลย

```markdown
✅ สิ่งที่ควรอยู่ใน CLAUDE.md
- ภาษาที่ใช้ตอบ (ไทย/English)
- persona ("คุณคือ Senior iOS Developer")
- hard rules ที่ใช้กับทุก task
- pointer ไปหาไฟล์อื่น (@import หรือ path)

❌ สิ่งที่ไม่ควรอยู่ใน CLAUDE.md
- ขั้นตอนการทำงานเฉพาะ task → ย้ายไป skills/
- รายละเอียด architecture → ย้ายไป context.md
- code snippet หรือ example → ย้ายไป skills/
- ข้อมูลที่ใช้เฉพาะบาง task → โหลดเมื่อจำเป็นเท่านั้น
```

**Pointer pattern ที่แนะนำ:**
```markdown
# CLAUDE.md
ภาษา: ตอบเป็นภาษาไทย ใช้ English สำหรับ technical term
Persona: Senior iOS Developer ที่รู้จัก VIPER และ RxSwift

## Project context
@context.md

## Skills available
- review-code: @.claude/skills/review-code.md
- create-test: @.claude/skills/create-unit-test.md
- create-feature: @.claude/skills/create-feature.md
```

---

## ข้อ 10 — ระวัง Sensitive Information

*(จาก Anthropic blog โดยตรง)*

CLAUDE.md กลายเป็นส่วนหนึ่งของ system prompt
ถ้า commit ขึ้น git = ทุกคนที่มี repo access เห็นได้

```markdown
❌ ห้ามใส่ใน MD file เด็ดขาด
- API keys หรือ secret tokens
- database connection strings
- credentials หรือ passwords
- รายละเอียด security vulnerabilities ของระบบ
- internal IP addresses หรือ server details

✅ วิธีที่ถูกต้อง
- เก็บ secrets ใน .env หรือ CI/CD environment variables
- MD file บอกแค่ "ดึง API key จาก .env STRIPE_SECRET_KEY"
- ถ้า MD file มี sensitive info ให้ add ใน .gitignore
```

---

## ข้อ 11 — Size ที่เหมาะสม

ไม่มี hard limit แต่มี practical limit ที่ส่งผลต่อคุณภาพงาน

```
ไฟล์เดียว          → ไม่เกิน ~200 lines
                      ถ้าเกิน = responsibility ยังแยกไม่ถูก

รวมทุกไฟล์          → ไม่เกิน ~8,000 tokens ต่อ session
ที่โหลดพร้อมกัน       ถ้าเกิน = AI เริ่ม lose context ของกฎท้ายไฟล์
```

**สิ่งที่เกิดขึ้นจริงตาม token size:**
```
< 2,000 tokens   → อ่านครบ 100% ทุกครั้ง
2,000–8,000      → อ่านครบ แต่ท้ายไฟล์ได้ attention น้อยลง
> 8,000 tokens   → AI เริ่ม summarize แทนอ่าน
                   กฎที่อยู่ท้ายไฟล์มีโอกาสถูกข้ามสูง
```

**แก้ด้วย Progressive Disclosure:**
```markdown
# CLAUDE.md (สั้น — โหลดทุก session)
โหลดเฉพาะ hard rules และ pointer

# context.md (กลาง — โหลดเมื่อ review/code เริ่ม)
architecture และ project knowledge

# skills/*.md (โหลดเฉพาะเมื่อ trigger ตรง)
ขั้นตอนเฉพาะ task
```

---

## ข้อ 12 — Treat as Living Document

*(จาก explainx.ai — "Update Regularly")*

MD file เก่าคืออันตราย — AI จะทำตามข้อมูลที่ผิด
และยิ่งโปรเจกต์ใหญ่ขึ้น ความเสียหายจาก outdated context ยิ่งมาก

```markdown
## เมื่อไหร่ต้องอัปเดต
- เปลี่ยน min iOS/Android version
- เพิ่มหรือเปลี่ยน external service หรือ SDK
- เปลี่ยน architecture decision
- เพิ่ม hard rule ใหม่จาก retrospective
- เปลี่ยน directory structure
- เมื่อ AI ทำผิดซ้ำ ๆ ในจุดเดิม (= rule ยังไม่ชัดพอ)

## ท้ายทุกไฟล์ให้มีเสมอ
_Last updated: YYYY-MM-DD | By: [ชื่อ] | Reason: [เหตุผล]_
```

---

## ข้อ 13 — MD File อย่างเดียวไม่พอสำหรับ Critical Rules

*(จาก GitHub community research — compliance data)*

MD file guidance ได้ compliance จริงแค่ **25–40%**
ถ้าต้องการ enforce จริงต้องเสริมด้วย automated tools

```
MD file เพียงอย่างเดียว    → 25–40% compliance
MD file + linter/hooks     → ~95% compliance
```

**วิธีเสริม enforcement:**
```markdown
สำหรับ iOS:
- SwiftLint rules enforce naming และ style
- Xcode build phase script ตรวจ coverage
- GitLab CI block merge ถ้า test fail

สำหรับ React Native / TypeScript:
- ESLint + Prettier enforce code style
- Husky pre-commit hook รัน lint ก่อน commit
- GitHub Actions block PR ถ้า test fail
```

**หลักคือ:** ใช้ MD file บอก AI ว่า "ทำอะไร" แต่ใช้ automated tools enforce ว่า "ทำจริง"

---

## Checklist ก่อน Commit MD File

```
□ ทุกบรรทัด actionable — AI เปลี่ยนพฤติกรรมได้ทันที
□ มี path จริง ไม่ใช่แค่ชื่อ
□ hard rules แยกออกจาก preferences ชัดเจน
□ ทุก rule มี Why กำกับ ไม่ใช่แค่ What
□ ไม่มี general best practice ที่ AI รู้อยู่แล้ว
□ ไม่มี code snippet ที่อาจ out-of-date (ชี้ไปไฟล์จริงแทน)
□ ไม่มี sensitive info (API key, credentials, secrets)
□ ไฟล์นี้ตอบคำถามเดียว ไม่ปนกับไฟล์อื่น
□ ขนาดไม่เกิน ~200 lines
□ อัปเดต last updated date แล้ว
□ ถ้าเอาไฟล์นี้ออก AI จะทำงานผิดทันที (ถ้าไม่ใช่ = ไม่จำเป็น)
```

---

## สรุป 13 ข้อในบรรทัดเดียว

| ข้อ | หลักการ |
|---|---|
| 1 | เขียนให้ AI อ่าน — ไม่มี implicit ต้องบอกทุกอย่าง |
| 2 | Actionable ทุกบรรทัด — เอาออกแล้ว AI ต้องทำงานผิด |
| 3 | ห้าม/ต้อง ชัดเจน — ห้ามใช้คำคลุมเครือ |
| 4 | Path จริงเสมอ — ชื่ออย่างเดียวไม่พอ |
| 5 | ไม่ซ้ำ AI — เฉพาะ project-specific เท่านั้น |
| 6 | Explain Why — AI จะ apply rule ถูกใน edge case |
| 7 | ไม่ใส่ code snippet — ชี้ไปไฟล์จริงแทน |
| 8 | แยก responsibility ให้ถูกไฟล์ — context vs skills vs CLAUDE |
| 9 | CLAUDE.md สั้นที่สุด — โหลดทุก session ต้องกระชับ |
| 10 | ไม่มี sensitive info — MD file เป็น public document |
| 11 | Size พอดี — ~200 lines/file, ~8,000 tokens/session |
| 12 | Living document — เก่า = อันตราย อัปเดตสม่ำเสมอ |
| 13 | MD file + automated tools — อย่าพึ่ง MD อย่างเดียว |

---

## แหล่งอ้างอิง

| แหล่ง | URL |
|---|---|
| Anthropic Official Blog | https://claude.com/blog/using-claude-md-files |
| HumanLayer Blog | https://www.humanlayer.dev/blog/writing-a-good-claude-md |
| Builder.io | https://www.builder.io/blog/claude-md-guide |
| DeployHQ Blog | https://www.deployhq.com/blog/ai-coding-config-files-guide |

---

_Last updated: 2025-06-22 | Version: 1.1 | Reason: เพิ่มข้อ 6-13 จากแหล่งอ้างอิง_
