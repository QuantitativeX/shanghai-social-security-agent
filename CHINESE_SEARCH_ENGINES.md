# 中文搜索引擎验证指南 | Chinese Search Engine Verification Guide

## 🔍 百度 (Baidu) 验证

### 步骤 1: 访问百度搜索资源平台

1. 前往 [百度搜索资源平台](https://ziyuan.baidu.com/)
2. 使用百度账号登录（如果没有账号，需要注册）

### 步骤 2: 添加网站

1. 点击 "站点管理" → "添加网站"
2. 输入您的网站 URL：
   ```
   https://github.com/QuantitativeX/shanghai-social-security-agent
   ```
3. 选择网站类型："其他"

### 步骤 3: 选择验证方式

百度提供三种验证方式，推荐选择："文件验证"
- 百度会生成一个验证文件（通常命名为 `baidu_verify_xxxxx.html`）
- 下载此文件

### 步骤 4: 添加验证文件到仓库

1. 将下载的文件（例如 `baidu_verify_xxxxx.html`）放在：
   - **根目录**：`baidu_verify_xxxxx.html`
   - **文档目录**：`docs/baidu_verify_xxxxx.html`

2. 提交至 Git：
   ```bash
   git add baidu_verify_xxxxx.html docs/baidu_verify_xxxxx.html
   git commit -m "feat: add Baidu search verification files"
   git push
   ```

### 步骤 5: 在百度验证

回到百度搜索资源平台，点击"验证"，系统会自动检查文件

---

## 🔎 搜狗 (Sogou) 验证

### 步骤 1: 访问搜狗网站管理平台

1. 前往 [搜狗网站管理平台](https://zhanzhang.sogou.com/)
2. 使用搜狗账号登录（也可使用其他方式登录）

### 步骤 2: 添加网站

1. 点击 "网站管理" → "添加网站"
2. 输入您的网站 URL：
   ```
   https://github.com/QuantitativeX/shanghai-social-security-agent
   ```

### 步骤 3: 选择验证方式

搜狗提供多种验证方式，推荐选择："文件验证"
- 搜狗会生成一个验证文件（通常命名为 `sogousiteverification_xxxxx.txt` 或类似）
- 下载此文件

### 步骤 4: 添加验证文件到仓库

1. 将下载的文件放在：
   - **根目录**：`sogousiteverification_xxxxx.txt`
   - **文档目录**：`docs/sogousiteverification_xxxxx.txt`

2. 提交至 Git：
   ```bash
   git add sogousiteverification_xxxxx.txt docs/sogousiteverification_xxxxx.txt
   git commit -m "feat: add Sogou search verification files"
   git push
   ```

### 步骤 5: 在搜狗验证

回到搜狗网站管理平台，点击"验证"，系统会自动检查文件

---

## 📋 完整检查清单 | Complete Checklist

### 搜索引擎验证状态 | Search Engine Verification Status

```
✅ Google     - google67b5b09fc1f43d5a.html
✅ Bing       - BingSiteAuth.xml
⏳ Baidu      - baidu_verify_xxxxx.html (待添加)
⏳ Sogou      - sogousiteverification_xxxxx.txt (待添加)
```

### 文件位置 | File Locations

```
JobInsurance/
├── google67b5b09fc1f43d5a.html           ✅ Google (root)
├── BingSiteAuth.xml                      ✅ Bing (root)
├── baidu_verify_xxxxx.html               ⏳ Baidu (root)
├── sogousiteverification_xxxxx.txt       ⏳ Sogou (root)
├── docs/
│   ├── google67b5b09fc1f43d5a.html       ✅ Google (GitHub Pages)
│   ├── BingSiteAuth.xml                  ✅ Bing (GitHub Pages)
│   ├── baidu_verify_xxxxx.html           ⏳ Baidu (GitHub Pages)
│   └── sogousiteverification_xxxxx.txt   ⏳ Sogou (GitHub Pages)
```

---

## 🌐 搜索引擎验证优先级 | Priority

| 搜索引擎 | 全球市场份额 | 中国市场份额 | 优先级 |
|---------|-----------|----------|------|
| Google | 90%+ | 10%* | ✅ 完成 |
| Bing | 3%+ | 1%* | ✅ 完成 |
| Baidu | - | 70%+ | 🔴 高优先级 |
| Sogou | - | 10%+ | 🟡 中优先级 |

*中文搜索在中国由于政策原因，Google/Bing 流量受限。Baidu 和 Sogou 专注服务中文用户。

---

## 💡 最佳实践 | Best Practices

### ✅ Do's

- ✅ 两个位置都添加验证文件（根目录 + docs 目录）
- ✅ 文件名保持精确，不要修改或缩写
- ✅ 使用官方平台生成的文件，不要手动创建
- ✅ 验证成功后记录时间
- ✅ 定期检查各平台的爬虫活动

### ❌ Don'ts

- ❌ 不要修改或编辑验证文件的内容
- ❌ 不要使用错误的文件名
- ❌ 不要删除已验证的文件
- ❌ 不要在 .gitignore 中忽略这些文件

---

## 📊 验证后的下一步 | After Verification

验证成功后，在各平台配置：

### Baidu 配置
1. 提交站点地图 (Sitemap)
2. 设置爬虫访问频率
3. 配置链接提交方式
4. 开启数据推送

### Sogou 配置
1. 提交网站地图
2. 添加死链提交
3. 开启 URL 提交

---

## 📞 官方链接 | Official Links

- **百度搜索资源平台**: https://ziyuan.baidu.com/
- **搜狗网站管理平台**: https://zhanzhang.sogou.com/
- **Google Search Console**: https://search.google.com/search-console
- **Bing Webmaster Tools**: https://www.bing.com/webmasters

---

**提示**: 在您完成百度和搜狗的验证文件添加后，请告诉我文件名，我会帮您提交到 Git 仓库。

**Tip**: Once you have completed the verification files for Baidu and Sogou, please let me know the filenames and I'll help you submit them to the Git repository.
