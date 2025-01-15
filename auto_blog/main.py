# chat gpt api

import openai

# API 키 설정
openai.api_key = "YOUR_API_KEY"  # 생성한 API 키를 입력

# API 요청
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # 모델 선택
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "안녕하세요! ChatGPT API는 어떻게 사용하나요?"}
    ],
    max_tokens=100,  # 응답 길이 제한
    temperature=0.7,  # 창의성 조절
)

# 결과 출력
print(response["choices"][0]["message"]["content"])
