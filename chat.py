from openai import OpenAI
import json
import os
import sys


def main():
    data = {}
    path = ""
    jsonPath = ""
    try:
        path = os.environ["SNAP_DATA"]
        print(f"SNAP_DATA found: {path}")
    except KeyError:
        print("Error: not running in a snap environment.")
        sys.exit(1)

    jsonPath = path + "/share/connection.json"
    try:
        with open(jsonPath) as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: connection.json file not found in {jsonPath}")
        sys.exit(1)

    print(f"json data: {data}")
    url = data["openai"]
    print(f"Using OpenAI endpoint: {url}")
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
    print("Response received")

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
