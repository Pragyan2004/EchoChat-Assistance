import os
from groq import Groq

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("❌ GROQ_API_KEY environment variable is not set")

client = Groq(api_key=API_KEY)

def get_llm_answer(title, description, reviews, question):
    reviews_text = "\n".join(reviews[:5]) if reviews else "No reviews."
    prompt = (
        f"Product:\n{title}\n\n"
        f"Description:\n{description}\n\n"
        f"Reviews:\n{reviews_text}\n\n"
        f"Question: {question}\nAnswer briefly."
    )
    try:
        resp = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.3,
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        return f"Error contacting server: {e}"
