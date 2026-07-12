# Correction Decisions

Summary of high-confidence corrections applied to production references. Citations should be resolved through `term-index/<module>.json` and `evidence-cards.jsonl`; machine-specific paths are not used here.

## Audit Scope

- 2026-07-12 对用户提供的 11 份 PDF 做了全文抽取与交叉检索，覆盖针灸、黄帝内经、神农本草、伤寒论、金匮要略、仲景心法 6 个模块。
- 本轮只自动落地“PDF 可直接支持”或“规范术语且有跨 PDF 佐证”的高置信修正；不根据猜测改方名、药名、穴名或剂量。
- 临床案例、八纲辨证等无对应 PDF 的模块，仅修正能由上述 PDF 交叉证明的共用术语；天纪、扶阳论坛、易筋经、梁冬对话、斯坦福演讲等模块不在本轮 PDF 全文校验覆盖内。
- `evidence-cards.jsonl` 与 `term-index/*.json` 属源证据摘录层，其中的原始排印、OCR 或异体字不作机械改写；规范化结论记录在本文件和生产引用文件中。

## Applied Corrections With PDF Evidence

| Before | After | Public evidence |
| --- | --- | --- |
| `大气浓汤` | `大青龙汤` | `pdf-evidence:57bd28cae94e#p33`; also see Shang Han Lun cards under `term-index/shanghan.json` for `大青龙汤`. |
| `代者石` | `代赭石` | `pdf-evidence:e993d4602e6f#p109`; screenshot cross-check: `references/clinical-cases-screenshot-evidence.md` uses `代赭石`. |
| `苦主发散燥湿` | `苦主泻/坚/燥` | `pdf-evidence:57bd28cae94e#p69` for 苦味能泻/燥/坚; `pdf-evidence:d91c6e1e158c#p161` for 辛味发散、酸味收敛. |
| `溶穴` | `荥穴` | `pdf-evidence:24767a80968b#p78` for 荥穴属性; `pdf-evidence:24767a80968b#p156` for 行间穴. |
| `三黄穴` | `三皇穴` | `pdf-evidence:24767a80968b#p211`. |
| `盲虫` | `虻虫` | `pdf-evidence:fcf026a0b4f9#p91`; `pdf-evidence:a47aeb66677d#p67`. |
| `芘胡` | `茈胡` | `pdf-evidence:e993d4602e6f#p7`. |
| `遗精失惊` | `梦遗失精` | `pdf-evidence:e993d4602e6f#p27`. |
| `下交` | `下焦` | `pdf-evidence:1ae6e7523f17#p238`. |
| `独活（姜活）` | `独活（羌活）` | `pdf-evidence:57bd28cae94e#p79`. |
| `白蒿（石蒿）` | `白蒿` | `pdf-evidence:57bd28cae94e#p99` 明确说明“不是石蒿，是白蒿”。 |
| `水生萋蒿` | `水生蒌蒿`（PDF 注文）/`水生白蒿`（课程口语） | `pdf-evidence:57bd28cae94e#p99`; “萋蒿”未获 PDF 支持。 |
| 苓桂术甘汤方证混入“脐下悸” | 苓桂术甘汤对应“心下逆满、气上冲胸、起则头眩”；苓桂甘枣汤对应“脐下悸、欲作奔豚” | `pdf-evidence:58423f817a06#p75`; `pdf-evidence:58423f817a06#p77`. |
| 《仲景心法》第六讲主讲人写成“李教授” | `倪海厦` | PDF 题名与全篇课程语境；课程术语可交叉核对 `pdf-evidence:a47aeb66677d#p7`、`#p19`、`#p74`. |
| `无语众医` | 删除 | 未见于《仲景心法》PDF；对应段仅有阴阳诊断及手掌/手背温度说明，见 `pdf-evidence:a47aeb66677d#p19`. |
| 酒风方将“麋衔”直接混写为“鹿衔草” | `麋衔`；另注同步文稿作“糜衔”，课中释作茜草/鹿蹄草 | `pdf-evidence:1ae6e7523f17#p221`; 保留经典方名、文稿异文与课堂解释三个层级。 |
| 五输穴写成“井、荣、俞、经、合” | `井、荥、输、经、合` | `pdf-evidence:24767a80968b#p78`; “俞穴”另指背俞穴等语境，不与五输穴的“输”混写。 |
| 第五椎误标为肺俞 | 第五椎为心俞/课程心脏观察点；肺俞在第三椎 | `pdf-evidence:cf77b3ca01e5#p94`; `pdf-evidence:cf77b3ca01e5#p95`. |
| `红斑性囊疮/囊伤` | `红斑性狼疮` | 规范病名；课程 PDF 亦作“红斑性狼疮”，见 `pdf-evidence:cf77b3ca01e5#p96`. |
| `大黄蛰虫丸/蛰虫` | `大黄䗪虫丸/䗪虫`（PDF 排印作“蟅”） | `pdf-evidence:fcf026a0b4f9#p79`; 区分规范方名与 PDF 字形。 |
| `耳针心液` | 耳部`心点/心脏点` | `pdf-evidence:cf77b3ca01e5#p197`. |
| `软骨穴` | `然谷穴`（同段并见涌泉） | `pdf-evidence:cf77b3ca01e5#p179`; PDF 的同类肾经循行痛示例明确写“然谷、涌泉”。 |
| `红刮/蟹白/紫石` | 删除噪声；相关规范药名按原段分别核为`川红花/薤白/栝蒌实`等 | `pdf-evidence:fcf026a0b4f9#p302`; 不把破碎词强行一一映射。 |
| `瓜蒌石/圈牛` | 删除破碎药名，按同一病例 PDF 可核方药重写 | `pdf-evidence:fcf026a0b4f9#p302`. |
| `陆风子/路风子` | `瓦楞子` | `pdf-evidence:a47aeb66677d#p26`; `pdf-evidence:fcf026a0b4f9#p320`. |

## Applied Corrections With Public Non-PDF Evidence

| Before | After | Public evidence |
| --- | --- | --- |
| `破菌/连针破金` | `破军/廉贞破军` | `references/tianji-screenshot-evidence.md` includes the relevant `廉贞 破军` board note; `references/tianji.md` repeatedly indexes `破军` in the same lesson family. |

## Corrections Needing Source Evidence

| Before | After | Evidence gap |
| --- | --- | --- |
| `易肝散` | `抑肝散` | Correction follows course transcript context, but no PDF/screenshot evidence card is available yet. Treat as evidence-limited until a source card is added. |
| `阳宅穴` | `阳宅学` | Correction follows Tianji context and same-module usage, but no independent PDF/screenshot card is available yet. Treat as evidence-limited until a source card is added. |

## Evidence-Limited Items

| Item | Reason not auto-corrected |
| --- | --- |
| `瓜萋10g` | 疑似 `瓜蒌/瓜蔞實`，但缺少逐字唯一证据。 |
| 天纪部分星曜句 | ASR 破碎，需要逐句对照板书或视频。 |
| 源文件名中的 `倪海夏...` | 对应旧抽文本/源索引文件名，未同步规范源文件前不改。 |
