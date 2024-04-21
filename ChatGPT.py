from openai import OpenAI
from config import OPENAI_API_KEY
client = OpenAI(
    api_key=OPENAI_API_KEY,
)


async def gpt(promt: str) -> str:
    try:
        message = []
        question = [
            {"role": "system", "content": "You are a helpful assistant City Pass Astana Bot."},
            {"role": "user", "content": f"{promt}"}
        ]
        message.extend(question)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=message,
            temperature=0
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
