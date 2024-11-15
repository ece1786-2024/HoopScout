# Data Extration Agent
from openai import OpenAI

client = OpenAI(api_key="API_KEY")

prompt = """
your prompt
"""

def DE_agent_response(statement):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": statement}
        ]
    )

    reply = response.choices[0].message.content.strip()
    return reply

if __name__ == "__main__":
    print("Unit test here")