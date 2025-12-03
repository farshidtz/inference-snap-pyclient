import json
import os
import sys
from openai import OpenAI
from openai import APIConnectionError


def main():
    data = {}
    path = ""
    jsonPath = ""
    url = ""
    try:
        path = os.environ["SNAP_DATA"]
    except KeyError:
        print("Error: not running in a snap environment.", file=sys.stderr)
        sys.exit(1)

    jsonPath = path + "/inference-snap/status/status.json"
    try:
        with open(jsonPath) as f:
            data = json.load(f)
        print(f"Status: {data}")
        url = data["endpoints"]["openai"]
    except FileNotFoundError:
        print(
            f"Error: status file not found at {jsonPath}",
            file=sys.stderr,
        )
        sys.exit(1)
        
    print(f"Using OpenAI endpoint: {url}")
    try:
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
    except APIConnectionError as e:
        print(f"Error: unable to connect to {url}", file=sys.stderr)
        print(f"Details: {e}", file=sys.stderr)
        sys.exit(1)

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
