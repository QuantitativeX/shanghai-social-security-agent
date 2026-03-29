## 贡献指南 | Contributing Guide

感谢你对 shanghai-unemployment-advisor 的支持！我们欢迎各种形式的贡献，无论是改进文档、报告问题、还是提交新功能。

Thank you for supporting shanghai-unemployment-advisor! We welcome contributions of all kinds, whether it's improving documentation, reporting issues, or submitting new features.

---

## 如何贡献 | How to Contribute

### 1. 报告问题 | Report Issues

如果你发现政策信息过期、答案不准确或有其他问题，请：

1. 查看 [Issues](../../issues) 是否已有相同问题
2. 创建新 Issue，标题清晰，描述详细
3. 包含以下信息：
   - 问题分类（`bug`, `policy-update`, `documentation`, etc.）
   - 具体场景和复现步骤（如适用）
   - 相关政策文件或官方链接
   - 系统信息（如适用）

**示例**:
```
标题: 2026年失业金支付标准需要更新
分类: policy-update
描述: 根据上海市人力资源和社会保障局网站，2026年Q2失业金标准已调整为2400元/月，但本项目仍显示2305元/月。
附件: 官方链接链接
```

### 2. 改进政策内容 | Improve Policy Content

政策信息是本项目的核心。如果你发现信息过期或需要补充：

1. Fork 本仓库
2. 创建分支：`git checkout -b feature/update-policy-<specific-topic>`
3. 编辑相关文件：
   - `shanghai-unemployment-advisor/references/policy-guide.md` - 结构化政策知识库
   - `shanghai-unemployment-advisor/references/jobqa.md` - 常见问题库
   - `shanghai-unemployment-advisor/references/source.md` - 资源链接
4. 提交清晰的 Commit 信息
5. 创建 Pull Request，描述你的更改

**编辑要求**:
- ✅ 所有信息基于官方政策文件或权威媒体
- ✅ 标注政策适用期间（如 2025-2026）
- ✅ 提供官方链接或来源
- ✅ 保持格式一致性和双语对照

### 3. 改进代码 | Improve Code

欢迎优化脚本和工具：

1. Fork 本仓库
2. 创建分支：`git checkout -b feature/<feature-name>`
3. 提交代码更改（保持风格一致）
4. 编写/更新相关测试（如适用）
5. 创建 Pull Request

**代码要求**:
- Python 3.9+ 兼容
- 不引入额外依赖（仅使用标准库）
- 代码注释清晰（中英文均可）
- 通过现有的测试

### 4. 改进文档 | Improve Documentation

帮助改进 README、SKILL.md 或其他文档：

1. 修正错字、语法、翻译问题
2. 改进清晰度和结构
3. 添加使用示例
4. 更新过时信息

---

## 提交 Pull Request

### 前置条件

- 确保你的分支基于最新的 `main` 分支
- 本地测试无误
- 更新 CHANGELOG.md（如涉及功能变更）

### PR 描述模板

```markdown
## 描述 | Description

简要说明这个 PR 的目的。

## 类型 | Type

- [ ] 政策内容更新 (policy content update)
- [ ] 代码改进 (code improvement)  
- [ ] 文档更新 (documentation)
- [ ] 错误修复 (bug fix)

## 相关问题 | Related Issues

关闭 #issue_number

## 更改详情 | Changes Made

列出具体改动，如：
- 修复了失业金标准数据
- 更新了4050补贴申请流程
- 优化了网页抓取脚本

## 验证方式 | How Has This Been Tested?

说明你如何验证这些更改（政策验证链接、测试场景等）

## 检查清单 | Checklist

- [ ] 代码遵循本项目的风格指南
- [ ] 已自我审查代码
- [ ] 已注释代码（特别是复杂逻辑）
- [ ] 文档已更新（如适用）
- [ ] 未添加产生新警告的更改
- [ ] 新增功能已添加相应文档
- [ ] 所有政策信息来源明确
```

---

## 开发指南 | Development Guide

### 项目结构

```
shanghai-unemployment-advisor/
├── SKILL.md                  # 技能定义和工作流程
├── references/
│   ├── policy-guide.md       # 政策知识库（修改这里来更新政策）
│   ├── jobqa.md              # FAQ 库
│   └── source.md             # 官方资源链接
└── scripts/
    └── fetch_policy.py       # 网页抓取工具
```

### 常见任务

#### 更新政策信息

编辑 `shanghai-unemployment-advisor/references/policy-guide.md`:
```markdown
## 失业保险金 | Unemployment Insurance

### 支付标准 Payment Standard
- **2025-2026 月标准**: 2305 元 (更新此处)
- **官方链接**: (提供链接)
```

#### 添加新的 FAQ

编辑 `shanghai-unemployment-advisor/references/jobqa.md`:
```markdown
### Q: 你的新问题是什么？
A: 详细答案和相关链接...
```

#### 添加新的资源链接

编辑 `shanghai-unemployment-advisor/references/source.md`:
```markdown
2. [具体资源标题] - 描述 | Description  
   URL: https://...  
   适用范围: 失业金 / 灵活就业 / ...
```

---

## 社区准则 | Community Guidelines

### 我们的承诺

我们承诺创建一个热情和包容的社区，所有成员无分种族、民族、性别、性取向、国籍或宗教信仰。

### 期望行为

- 使用欢迎和包容的语言
- 尊重不同的观点和经验
- 接受建设性批评
- 关注对社区最有利的事情
- 对其他社区成员表示同情

### 不可接受的行为

- 骚扰、歧视或辱骂他人
- 发布他人的私人信息
- 其他可合理认为不当的行为

---

## 获取帮助 | Getting Help

- 📖 查看 [README.md](README.md) 了解项目概况
- 📋 查看 [SKILL.md](shanghai-unemployment-advisor/SKILL.md) 了解技能工作流
- 💬 在 [Discussions](../../discussions) 中提问
- ☎️ 参考官方资源：12333 热线或随申办 APP

---

## 许可 | License

通过贡献代码，你同意你的贡献将在 MIT 许可下授权。

---

感谢你的贡献！您的帮助使这个项目对更多 Shanghai 地区的人有价值。

Thank you for contributing! Your help makes this project valuable to more people in Shanghai!
