from openai import OpenAI
def summerize(text):
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Tu es un outil permettant de résumé des messages vocaux à partir d'une transcription."},
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return completion.choices[0].message.content