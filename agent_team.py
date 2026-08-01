#!/usr/bin/env python3
"""
三模型协作 Demo：DeepSeek（写代码）+ Kimi（审代码）+ Qwen（写文档）
三个国产模型组队干活，全程无需翻墙、无需美元信用卡。
=============================================
使用方法：
  1. pip install openai
  2. 设置环境变量（去各平台免费注册获取 API Key）：
     export DEEPSEEK_API_KEY="sk-xxx"
     export KIMI_API_KEY="sk-xxx"
     export DASHSCOPE_API_KEY="sk-xxx"
  3. python3 agent_team.py "你的任务描述"
"""

import os, sys, json
from openai import OpenAI

# ─── 三个模型的客户端 ─────────────────────────────
clients = {
    "deepseek": OpenAI(
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com",
    ),
    "kimi": OpenAI(
        api_key=os.getenv("KIMI_API_KEY"),
        base_url="https://api.moonshot.cn/v1",
    ),
    "qwen": OpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    ),
}

# ─── 模型角色定义 ─────────────────────────────────
ROLES = {
    "deepseek": {
        "model": "deepseek-chat",
        "role": "首席工程师（写代码）",
        "system": "你是一个资深 Python 工程师。只输出代码，不要废话。代码要简洁、可运行、有注释。",
    },
    "kimi": {
        "model": "moonshot-v1-8k",
        "role": "代码审查员（审代码）",
        "system": "你是一个严格的代码审查员。审查以下代码，指出：1) bug 2) 安全问题 3) 改进建议。用中文简洁回复。如果代码没问题就说「代码审查通过✅」。",
    },
    "qwen": {
        "model": "qwen-plus",
        "role": "技术文档官（写文档）",
        "system": "你是一个技术文档撰写者。根据代码和审查意见，写一份简洁的 README 文档，包含：功能说明、安装方法、使用示例。用中文写。",
    },
}


def call_model(name: str, prompt: str) -> str:
    """调用指定模型"""
    cfg = ROLES[name]
    client = clients[name]
    resp = client.chat.completions.create(
        model=cfg["model"],
        messages=[
            {"role": "system", "content": cfg["system"]},
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
        max_tokens=2048,
    )
    return resp.choices[0].message.content


def main():
    task = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "写一个 Flask 网页应用，访问 /time 返回当前北京时间"

    print("=" * 60)
    print(f"🤖 AI 团队启动！任务：{task}")
    print("=" * 60)

    # ── 阶段1：DeepSeek 写代码 ──
    print("\n📝 [阶段1] DeepSeek（首席工程师）正在写代码...")
    code = call_model("deepseek", f"任务：{task}\n请写完整的可运行代码：")
    print(f"\n{code[:800]}{'...' if len(code) > 800 else ''}")

    # ── 阶段2：Kimi 审代码 ──
    print("\n\n🔍 [阶段2] Kimi（代码审查员）正在审查代码...")
    review = call_model("kimi", f"请审查以下代码：\n```python\n{code}\n```")
    print(f"\n{review[:600]}{'...' if len(review) > 600 else ''}")

    # ── 阶段3：Qwen 写文档 ──
    print("\n\n📖 [阶段3] Qwen（文档官）正在写 README...")
    doc = call_model("qwen", f"""代码：
```python
{code}
```

审查意见：
{review}

请写一份 README 文档。""")
    print(f"\n{doc}")

    # ── 阶段4：Kimi 最终审查 ──
    print("\n\n✅ [阶段4] Kimi 最终审查...")
    final = call_model("kimi", f"""请对以下交付物做最终审查：
代码：```python\n{code}\n```
文档：{doc}

用 1-2 句话总结是否可以交付。""")
    print(f"\n{final}")

    # ── 汇总 ──
    output = {
        "task": task,
        "code": code,
        "review": review,
        "documentation": doc,
        "final_verdict": final,
    }

    # 保存结果
    with open("agent_team_output.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 60)
    print("🎉 团队交付完成！结果已保存到 agent_team_output.json")
    print("=" * 60)


if __name__ == "__main__":
    main()
