import json
import os
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
#from openai import OpenAI
from google import genai

load_dotenv()

SOURCE_URL = "https://betproof.co.za/casino-bonuses-south-africa/"
OUTPUT_FILE = Path("../data/bonuses.json")

TARGET_CASINOS = {
    "Hollywoodbets",
    "Betway South Africa",
    "Supabets",
}

#client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def fetch_page() -> str:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/154.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
    }

    response = requests.get(
        SOURCE_URL,
        timeout=30,
        headers=headers,
    )

    response.raise_for_status()
    return response.text


def extract_casinos(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table")

    if table is None:
        raise RuntimeError("Casino table was not found.")

    casinos = []

    for row in table.find_all("tr")[1:]:
        cells = row.find_all(["td", "th"])

        if len(cells) < 4:
            continue

        values = [
            cell.get_text(" ", strip=True)
            for cell in cells
        ]

        casino_name = (values[0].replace("Play", "").replace("→", "").strip()
)

        if casino_name not in TARGET_CASINOS:
            continue

        casinos.append(
            {
                "casino": casino_name,
                "bonusText": values[1],
                "wageringText": values[2],
                "minimumDeposit": values[3],
                "sourceUrl": SOURCE_URL,
            }
        )

    return casinos



def structure_bonus_with_ai(casino: dict) -> dict:
    prompt = f"""
Extract structured casino bonus information from the following source data.

Casino: {casino["casino"]}
Bonus text: {casino["bonusText"]}
Wagering text: {casino["wageringText"]}
Minimum deposit: {casino["minimumDeposit"]}

Return JSON with exactly these fields:

{{
  "welcomeBonus": "string",
  "wageringRequirement": number or null,
  "minimumDeposit": "string"
}}

Rules:
- welcomeBonus should contain the advertised welcome bonus.
- wageringRequirement should be the main numeric wagering multiplier.
- If multiple wagering multipliers exist, use the main casino/deposit bonus multiplier.
- Do not invent information.
- If a value cannot be determined, use null.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": {
                "type": "OBJECT",
                "properties": {
                    "welcomeBonus": {
                        "type": "STRING"
                    },
                    "wageringRequirement": {
                        "type": "NUMBER",
                        "nullable": True
                    },
                    "minimumDeposit": {
                        "type": "STRING"
                    }
                },
                "required": [
                    "welcomeBonus",
                    "wageringRequirement",
                    "minimumDeposit"
                ]
            }
        },
    )

    structured = json.loads(response.text)

    return {
        "casino": casino["casino"],
        "welcomeBonus": structured.get("welcomeBonus"),
        "wageringRequirement": structured.get("wageringRequirement"),
        "minimumDeposit": structured.get("minimumDeposit"),
        "sourceUrl": casino["sourceUrl"],
    }



def save_json(casinos: list[dict]) -> None:
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(casinos, file, indent=2, ensure_ascii=False)



def main() -> None:
    print("Fetching casino data...")

    html = fetch_page()
    raw_casinos = extract_casinos(html)

    if len(raw_casinos) != 3:
        raise RuntimeError(
            f"Expected 3 casinos, but found {len(raw_casinos)}."
        )

    print("Sending bonus terms to the language model...")

    structured_casinos = []

    for casino in raw_casinos:
        print(f"Processing: {casino['casino']}")

        structured = structure_bonus_with_ai(casino)
        structured_casinos.append(structured)

    save_json(structured_casinos)

    print()
    print(f"Successfully processed {len(structured_casinos)} casinos.")
    print(f"Saved to: {OUTPUT_FILE}")



if __name__ == "__main__":
    main()
