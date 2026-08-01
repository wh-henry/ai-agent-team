<p align="center">
  <img src="https://img.shields.io/badge/DeepSeek-写代码-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Kimi-审代码-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Qwen-写文档-orange?style=for-the-badge" />
</p>

<h1 align="center">🤖 AI Agent Team</h1>
<p align="center"><strong>三个国产模型组队干活：DeepSeek 写代码 + Kimi 审 Bug + Qwen 自动写文档</strong></p>

<p align="center">
  <img src="https://img.shields.io/badge/成本-每次_4分钱-success" />
  <img src="https://img.shields.io/badge/翻墙-不需要-red" />
  <img src="https://img.shields.io/badge/美元信用卡-不需要-red" />
  <img src="https://img.shields.io/badge/免费额度-够用几千次-brightgreen" />
</p>

---

## 它做什么

你只需要一行命令：

```bash
python agent_team.py "写一个网页显示北京时间"
```

然后你的 AI 团队就开始工作了：

```
👨‍💻 DeepSeek（首席工程师）→ 写出完整 Python 代码
🔍 Kimi（代码审查员）   → 检查 bug、安全问题、改进建议
📖 Qwen（文档官）       → 自动生成 README 文档
✅ Kimi（最终审查）     → 「代码和文档都没问题，可以交付」
```

---

## 为什么用三个模型而不是一个

| 单模型 | 三模型协作 |
|--------|-----------|
| 代码可能有隐藏 bug | 第二个模型帮你揪出来 |
| 写完还要自己写文档 | 自动生成 README |
| 改完不知道改好没好 | 审查员二次确认 |
| 全凭一个模型的理解 | 三个视角交叉验证 |

---

## 快速开始

### 1. 获取 API Key（免费，5 分钟）

| 模型 | 平台 | 免费额度 |
|------|------|---------|
| DeepSeek | [platform.deepseek.com](https://platform.deepseek.com) | 500 万 tokens |
| Kimi | [platform.moonshot.cn](https://platform.moonshot.cn) | 15 元 |
| Qwen | [dashscope.console.aliyun.com](https://dashscope.console.aliyun.com) | 100 万 tokens |

### 2. 安装

```bash
git clone https://github.com/YOUR_USERNAME/ai-agent-team.git
cd ai-agent-team
pip install openai
```

### 3. 设置 API Key

```bash
export DEEPSEEK_API_KEY="sk-你的key"
export KIMI_API_KEY="sk-你的key"
export DASHSCOPE_API_KEY="sk-你的key"
```

### 4. 运行

```bash
# 默认任务：写一个显示北京时间的网页
python agent_team.py

# 自定义任务
python agent_team.py "写一个命令行待办事项工具，支持添加、删除、列出"
```

---

## 定制你的团队

改几行 system prompt，可以搭出任何团队：

<details>
<summary>📝 AI 写文章团队</summary>

```python
ROLES = {
    "deepseek": {"role": "✍️ 初稿写手", "system": "根据主题写文章..."},
    "kimi":     {"role": "📝 编辑",     "system": "润色文章，修正语病..."},
    "qwen":     {"role": "🎨 标题优化", "system": "生成 5 个吸引人的标题..."},
}
```
</details>

<details>
<summary>📊 AI 炒股研究团队</summary>

```python
ROLES = {
    "deepseek": {"role": "📊 数据分析师", "system": "分析财务数据..."},
    "kimi":     {"role": "🏭 行业研究员", "system": "分析行业趋势..."},
    "qwen":     {"role": "📋 策略师",     "system": "综合给出投资建议..."},
}
```
</details>

<details>
<summary>🎯 AI 英语学习团队</summary>

```python
ROLES = {
    "deepseek": {"role": "🎯 口语老师", "system": "出 IELTS 题目并给范文..."},
    "kimi":     {"role": "🔍 语法检查员", "system": "检查语法错误..."},
    "qwen":     {"role": "📝 润色师",     "system": "改成更地道的表达..."},
}
```
</details>

---

## 成本

| 模型 | 价格（每百万 tokens） | 一次任务花费 |
|------|---------------------|------------|
| DeepSeek | ¥1 / ¥2 | ~0.003 元 |
| Kimi | ¥12 / ¥12 | ~0.03 元 |
| Qwen Plus | ¥2 / ¥6 | ~0.01 元 |

**总计：一次完整的「写代码 + 审查 + 写文档」约 4-5 分钱。**

---

## 原理

核心思想：**不找一个全能模型，而是让多个模型像团队一样协作。**

每个模型只需要做好一件事（写代码 / 审代码 / 写文档），通过流水线串联，三个「专才」的效果超过一个「通才」。

技术栈：所有模型都兼容 OpenAI API 格式，一个 `openai` 库全部搞定。

---

## 文件说明

```
ai-agent-team/
├── agent_team.py      # 主脚本
├── requirements.txt   # 依赖（只有 openai）
└── README.md         # 本文件
```

---

## 作者

一个正在用 AI 给自己打工的高中生。

---

## 支持

如果这个项目对你有帮助，欢迎 ⭐ Star！

也欢迎请我喝杯奶茶 ☕

<p align="center">
  <img src="https://img.shields.io/badge/微信赞赏-觉得有用就赏-brightgreen?style=flat-square" />
</p>
