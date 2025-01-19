import openai

# OpenAI API 키 설정
openai.api_key = ""  # 생성한 API 키를 입력

# 요청 메시지 구성
messages = [
    {"role": "system", "content": """
    You are an expert in writing blog posts. Please follow the steps below to create a blog post:

1. Create an SEO-optimized blog title that matches the keyword I provide.
2. Write detailed and well-structured blog content.
3. Create a horizontal image for the blog post.
4. Provide SEO-optimized hashtags.
    """},
    {"role": "user", "content": "일론 머스크"}
]

# API 호출
response = openai.chat.completions.create(
    model="gpt-4o-mini",  # 올바른 모델 이름 사용
    messages=messages,
)

# 응답 출력
print("AI의 응답:", response.choices[0].message.content)
