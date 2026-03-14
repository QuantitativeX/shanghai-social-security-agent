# 上海失业政策咨询 — Agent Skill

基于 [Agent Skills](https://agentskills.io/specification) 规范构建的智能体技能，专门解答 **2025-2026 年上海市失业保险与社保政策**问题，兼容所有支持 Agent Skills 标准的 AI 助手。

## 功能

- **失业保险金**：领取条件、金额标准、领取期限、申领流程
- **灵活就业社保**：参保方式、缴费比例与基数、线上办理指南
- **就业困难人员（4050）**：认定标准、社保补贴、退出机制
- **企业稳岗补贴**：一次性吸纳补贴、扩岗补助、个人社保补贴
- **在线资料抓取**：本地知识库不足时，自动从官方网站获取最新内容

## 安装

需要 **Python 3.9+**，无需安装额外依赖。

```bash
python install.py
```

运行后按提示选择安装范围和路径：

| 选项 | 说明 |
|------|------|
| `g` Global（全局） | 安装到用户主目录，所有项目可用 |
| `p` Project（项目） | 安装到当前目录，可通过 git 共享给团队 |
| `c` Custom（自定义） | 手动输入任意路径 |

### 各 Agent 安装路径参考

| Agent | 全局路径 | 项目路径 |
|-------|---------|---------|
| Cursor | `~/.cursor/skills/` | `.cursor/skills/` |
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| 通义灵码 Lingma | `~/.lingma/skills/` | `.lingma/skills/` |
| 自定义 | 手动输入任意路径 | — |

## 使用方式

安装完成后，直接用中文向支持该技能的 AI 助手提问：

```
上海失业金怎么领？
我被裁员了，社保怎么处理？
灵活就业社保一个月要交多少钱？
4050补贴申请条件是什么？
失业期间医保还有效吗？
```

## 技能结构

```
shanghai-unemployment-advisor/
├── SKILL.md                  # 技能入口与工作流程说明
├── references/
│   ├── policy-guide.md       # 2025-2026 上海就业社保政策知识库
│   ├── jobqa.md              # 15 类高频问题标准问答
│   └── source.md             # 官方在线资源链接列表
└── scripts/
    └── fetch_policy.py       # 网页内容抓取脚本（备用，纯标准库）
```

技能采用**渐进式披露**策略（符合 [agentskills.io](https://agentskills.io/specification) 规范）：

1. 启动时仅加载 `name` + `description`（~100 tokens）
2. 触发后加载 `SKILL.md` 正文
3. `references/` 文件按需读取，节省上下文

## 工作流程

```
用户提问
   │
   ▼
读取 references/policy-guide.md + references/jobqa.md
   │
   ├─ 已找到答案 ──→ 直接回答 + 附官方链接
   │
   └─ 内容不足 ───→ 读取 references/source.md
                        │
                        ▼
                    python scripts/fetch_policy.py "<URL>"
                        │
                        ▼
                    综合本地 + 在线内容回答
```

## 数据来源

政策内容整理自以下官方渠道（2025-2026 年数据）：

- 上海市人力资源和社会保障局（rsj.sh.gov.cn）
- 上海市"一网通办"平台（zwdt.sh.gov.cn）
- 12333 人社服务平台（m12333.cn）
- 上海本地宝（sh.bendibao.com）

> **免责声明**：本技能基于公开政策文件整理，具体执行细则以官方最新通知为准。建议通过「随申办」APP 或拨打 **12333** 热线核实。

## 许可证

MIT
