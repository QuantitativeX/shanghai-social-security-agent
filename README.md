# Agent Skill | 上海失业政策咨询助手 | Shanghai Unemployment & Social Security Advisor

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Agent Skills Compatible](https://img.shields.io/badge/Agent%20Skills-Compatible-green)](https://agentskills.io/specification)
[![GitHub Pages](https://img.shields.io/badge/🌐_Website-Visit-blue)](https://quantitativex.github.io/shanghai-social-security-agent/)

**🌐 [查看项目主页 · Visit Project Site](https://quantitativex.github.io/shanghai-social-security-agent/)**

**基于 Agent Skills 规范构建的智能体技能 | AI Agent Skill for Shanghai Unemployment Insurance & Social Security Policy Consultation**

专门解答 **2025-2026 年上海市失业保险、灵活就业社保、4050 补贴**等政策问题，兼容所有支持 [Agent Skills](https://agentskills.io/specification) 标准的 AI 助手（Cursor、Claude Code、通义灵码等）。

An intelligent agent skill built on [Agent Skills](https://agentskills.io/specification) specification, specializing in **2025-2026 Shanghai unemployment insurance, flexible employment social security, and 4050 subsidy policies**. Compatible with all AI assistants supporting Agent Skills standard (Cursor, Claude Code, Lingma, etc.).

## 🎯 核心功能 | Key Features

### 失业保险金咨询 | Unemployment Insurance Benefits
- **领取条件**：非本人意愿离职、缴费年限要求、失业登记流程
- **金额标准**：2025-2026 年最新支付标准（2305 元/月起）
- **领取期限**：根据累计缴费年限计算（最长 24 个月）
- **配套医保**：失业期间医疗保险由基金代缴

### 灵活就业社保 | Flexible Employment Social Security
- **参保方式**：线上办理（随申办 APP）、线下窗口
- **缴费比例**：养老 20% + 医疗 10%
- **缴费基数**：2025 年下限 7460 元/月，上限 37302 元/月
- **户籍政策**：已取消户籍限制，外地户籍也可参保

### 4050 就业困难人员补贴 | Employment Hardship Subsidy (4050 Policy)
- **认定标准**：女性 40 岁/男性 45 岁以上，失业满 6 个月
- **社保补贴**：按缴费基数 50% 给予补贴（约 1100-1200 元/月）
- **补贴期限**：最长 3 年，距退休不足 5 年可延长至退休
- **退出机制**：重新就业、创业后自动取消

### 企业稳岗补贴 | Enterprise Stabilization Subsidies
- **一次性吸纳就业补贴**：2000 元/人（招用失业人员或毕业生）
- **一次性扩岗补助**：1500 元/人（招用高校毕业生）
- **个人社保补贴**：重点行业企业可按 25% 给予补贴

### 智能在线更新 | Intelligent Online Updates
- **本地知识库**：包含 15 类高频问题标准问答
- **实时抓取**：自动从官方网站获取最新政策内容
- **渐进式披露**：优化上下文使用，节省 Token

## 🚀 快速开始 | Quick Start

### 环境要求 | Requirements
- **Python 3.9+** (No additional dependencies required)
- 支持平台：Windows / macOS / Linux

### 一键安装 | One-Click Installation

```bash
python install.py
```

运行后按提示选择安装范围和路径 | Select installation scope after running:

| 选项 Option | 说明 Description | 适用场景 Use Case |
|-------------|------------------|------------------|
| `g` Global（全局） | 安装到用户主目录，所有项目可用 | Personal use across all projects |
| `p` Project（项目） | 安装到当前目录，可通过 git 共享给团队 | Team collaboration via git |
| `c` Custom（自定义） | 手动输入任意路径 | Advanced users |

### 支持的 AI 助手 | Supported AI Agents

| Agent | 全局路径 Global Path | 项目路径 Project Path |
|-------|---------------------|----------------------|
| **Cursor** | `~/.cursor/skills/` | `.cursor/skills/` |
| **Claude Code** | `~/.claude/skills/` | `.claude/skills/` |
| **通义灵码 Lingma** | `~/.lingma/skills/` | `.lingma/skills/` |
| **自定义 Custom** | 手动输入任意路径 Manual path | — |

## 💬 使用示例 | Usage Examples

安装完成后，直接用**中文**或**English**向 AI 助手提问 | After installation, ask questions in **Chinese** or **English**:

### 常见问题 | Frequently Asked Questions

**失业保险金 | Unemployment Benefits**
```
上海失业金怎么领？ How to claim unemployment benefits in Shanghai?
我被裁员了，社保怎么处理？I was laid off, how to handle social security?
失业金一个月多少钱？How much is the monthly unemployment benefit?
失业金可以领多久？How long can I receive unemployment benefits?
```

**灵活就业社保 | Flexible Employment Social Security**
```
灵活就业社保怎么办理？How to apply for flexible employment social security?
灵活就业社保一个月要交多少钱？How much to pay monthly for flexible employment insurance?
外地户籍可以在上海交社保吗？Can non-Shanghai residents pay social security in Shanghai?
```

**4050 补贴 | 4050 Subsidy**
```
4050 补贴申请条件是什么？What are the eligibility requirements for 4050 subsidy?
女性 40 岁失业有什么福利？What benefits are available for unemployed women over 40?
就业困难人员怎么认定？How to apply for employment hardship recognition?
```

**企业补贴 | Enterprise Subsidies**
```
企业招用失业人员有补贴吗？Are there subsidies for hiring unemployed persons?
一次性吸纳就业补贴怎么申请？How to apply for one-time employment absorption subsidy?
```

## 📁 项目结构 | Project Structure

```
shanghai-unemployment-advisor/
├── SKILL.md                  # 技能入口与工作流程说明 | Skill entry point & workflow
├── references/
│   ├── policy-guide.md       # 2025-2026 上海就业社保政策知识库 | Policy knowledge base
│   ├── jobqa.md              # 15 类高频问题标准问答 | 15 categories of FAQs
│   └── source.md             # 官方在线资源链接列表 | Official resource links
└── scripts/
    └── fetch_policy.py       # 网页内容抓取脚本（纯标准库） | Web scraping script (stdlib only)
```

### 技术特点 | Technical Features

**渐进式披露策略 | Progressive Disclosure Strategy** (符合 [agentskills.io/specification](https://agentskills.io/specification))

1. **启动时 At startup**: 仅加载 `name` + `description`（~100 tokens）
2. **触发后 After trigger**: 加载 `SKILL.md` 正文
3. **按需读取 On-demand**: `references/` 文件按需读取，节省上下文

这种设计显著降低了 Token 消耗，提高了响应速度 | This design significantly reduces token consumption and improves response speed.

## 🔧 工作流程 | Workflow

```
用户提问 User Question
   │
   ▼
读取 Read references/policy-guide.md + references/jobqa.md
   │
   ├─ 已找到答案 Found ──→ 直接回答 + 附官方链接 Direct answer + official links
   │
   └─ 内容不足 Insufficient ───→ 读取 Read references/source.md
                                        │
                                        ▼
                                    python scripts/fetch_policy.py "<URL>"
                                        │
                                        ▼
                                    综合本地 + 在线内容回答 Synthesize local + online content
```

### 数据来源 | Data Sources

政策内容整理自以下**官方渠道**（2025-2026 年最新数据）| Policy content compiled from the following **official sources** (2025-2026 latest data):

- 🏛️ 上海市人力资源和社会保障局 (rsj.sh.gov.cn)
- 💻 上海市"一网通办"平台 (zwdt.sh.gov.cn)
- 📞 12333 人社服务平台 (m12333.cn)
- 📋 上海本地宝 (sh.bendibao.com)
- 📰 人民网、上观新闻等权威媒体 (People's Daily, ShObserver, etc.)

## ⚠️ 免责声明 | Disclaimer

> 本技能基于**公开政策文件**整理，具体执行细则以**官方最新通知**为准。
> 
> This skill is compiled based on **public policy documents**. For specific implementation details, please refer to the **latest official notices**.

**建议核实渠道 | Recommended Verification Channels:**
- 📱 「随申办」APP
- ☎️ 人社咨询热线 **12333**
- 🏢 街道社区事务受理中心

---

## 📄 许可证 | License

MIT License - See [LICENSE](LICENSE) file for details.

---

## 🔗 相关链接 | Related Links

- [🌐 项目主页 Project Website](https://quantitativex.github.io/shanghai-social-security-agent/) - 在线介绍页
- [Agent Skills Specification](https://agentskills.io/specification) - Agent Skills 技术规范
- [上海市人力资源和社会保障局](https://rsj.sh.gov.cn/) - Shanghai HR & Social Security Bureau
- [随申办 APP 下载](https://zwdt.sh.gov.cn/) - Shanghai Government Service Platform
- [12333 政策问答](https://m12333.cn/) - National Social Security Q&A Platform

---

## 📬 联系方式 | Contact

- **Repository**: [github.com/QuantitativeX/JobInsurance](https://github.com/QuantitativeX/JobInsurance)
- **Issues**: [Submit bugs or feature requests](https://github.com/QuantitativeX/JobInsurance/issues)
- **Discussions**: [Join discussions](https://github.com/QuantitativeX/JobInsurance/discussions)

---

## 🌟 关键词 | Keywords

**中文关键词**: 上海失业金、失业保险、灵活就业社保、4050 政策、就业困难人员、社保补贴、失业登记、随申办、裁员赔偿、离职证明

**English Keywords**: Shanghai unemployment benefits, unemployment insurance, flexible employment social security, 4050 policy, employment hardship, social security subsidy, unemployment registration, layoff compensation, China social security, AI agent skill

**技术标签**: #AgentSkills #AI #Python #Shanghai #Unemployment #SocialSecurity #Chatbot #Automation #OpenSource
