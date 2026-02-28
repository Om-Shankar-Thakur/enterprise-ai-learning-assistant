import os
from groq import Groq
from dotenv import load_dotenv
from app.prompt_template import build_system_prompt

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_chat_response(domain: str, user_message: str, learner_name: str = "Learner"):

    # No domain restriction anymore
    system_prompt = build_system_prompt(domain, learner_name)

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        return response.choices[0].message.content

    except Exception:
        return {
            "answer": f"Hi {learner_name}, I'm facing a temporary issue connecting to the AI service. Please try again.",
            "suggested_next_action": "Retry your question."
        }
