# SPDX-FileCopyrightText: 2025 Lincoln Wallace
# SPDX-License-Identifier: Apache-2.0

from openai import OpenAI
import json
import os
import sys


def main():
    data = {}
    path = ""
    jsonPath = ""
    url = ""
    try:
        path = os.environ["SNAP_DATA"]
        print(f"SNAP_DATA found: {path}")
    except KeyError:
        print("Error: not running in a snap environment.", file=sys.stderr)
        sys.exit(1)

    jsonPath = path + "/share/endpoints/endpoints.json"
    try:
        with open(jsonPath) as f:
            data = json.load(f)
        print(f"json data: {data}")
        url = data["openai"]
    except FileNotFoundError:
        print(
            f"Error: connection.json file not found in {jsonPath}, using default endpoint.",
            file=sys.stderr,
        )
        print("Defaulting to localhost:8324 - DeepSeek-r1 snap api endpoint.")
        url = "http://localhost:8324/v1"

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
