from openai import OpenAI


def main():
    url = "http://localhost:8080/v1"
    client = OpenAI(base_url=url, api_key="dummy_key")
    response = client.chat.completions.create(
        model="",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "Write a one-sentence bedtime story about a unicorn.",
            },
        ],
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
