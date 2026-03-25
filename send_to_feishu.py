import os
import requests

def send_feishu_msg(text):
    webhook = os.getenv("FEISHU_WEBHOOK")
    if not webhook:
        print("❌ 未配置 FEISHU_WEBHOOK，请检查 GitHub Secrets")
        return

    msg = {
        "msg_type": "text",
        "content": {"text": text}
    }

    try:
        resp = requests.post(webhook, json=msg)
        print("✅ 飞书消息发送成功，返回结果：", resp.text)
    except Exception as e:
        print("❌ 发送飞书消息失败，错误原因：", str(e))

if __name__ == "__main__":
    send_feishu_msg("📈 股票每日分析测试：GitHub Actions 手动触发成功！")
