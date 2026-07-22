# AI 编程自动化 · 接单示例仓库

> 用 **Codex + DeepSeek V4** 交付 Python / API / 爬虫 / 自动化脚本。  
> **下单与会员通道（爱发电）：** https://ifdian.net/a/my-worker

---

## 我能做什么

| 类型 | 示例 |
|------|------|
| Python 脚本 | 批处理、报表、文件整理 |
| API 开发 | FastAPI / Flask 脚手架、对接第三方 |
| 爬虫 | 列表采集、登录态、导出 CSV/JSON |
| 工程能力 | Bug 修复、代码迁移、性能优化、数据处理 |

**交付节奏：** 你出需求 → 我出代码，通常 **24 小时内**交付（复杂项目另议）。

---

## 怎么下单（推荐）

1. 打开爱发电主页：https://ifdian.net/a/my-worker  
2. 选择档位发电（或私信说明需求）  
3. 用本仓库的 [需求简报模板](templates/brief.md) 把需求发我  
4. 收到代码 / 仓库链接 / 使用说明

| 档位 | 价格 | 适合 |
|------|------|------|
| 请我喝瓶可乐 | ¥5/月 | 每月 1 个简单脚本（Python ≤50 行） |
| 编程助手 | ¥20/月 | 每月 3 个任务（API / 爬虫 / 数据处理） |
| 专属开发 | ¥100/月 | 每月更多任务或 1 个完整小项目 |

> 价格与权益以爱发电页面实时为准。

---

## 仓库里有什么

```
ai-coding-services/
├── README.md                 ← 你在看的这份
├── templates/brief.md        ← 下单用需求模板（复制填写）
└── examples/
    ├── python_script/        ← 批处理脚本骨架
    ├── api_scaffold/         ← 最小 FastAPI 骨架
    └── crawler_template/     ← 爬虫采集骨架
```

这些是**可运行的骨架**，用来演示风格与交付形态；正式需求按你的业务定制。

### 本地试跑（可选）

```bash
# Python 脚本
python examples/python_script/main.py --help

# API（需安装依赖）
cd examples/api_scaffold && pip install -r requirements.txt && uvicorn main:app --reload

# 爬虫骨架
python examples/crawler_template/crawl.py --help
```

---

## 接单范围 / 不接范围

**接：** 明确输入输出的脚本、小中型 API、合规数据采集、重构与修 Bug。  
**不接：** 绕过验证码/风控的灰色爬虫、破解、侵犯隐私或违法用途。

---

## 联系

- **爱发电（收款 + 排期）：** https://ifdian.net/a/my-worker  
- **GitHub：** https://github.com/z1302065902-cloud  

有需求先填 [templates/brief.md](templates/brief.md)，发电后把内容私信给我即可。
