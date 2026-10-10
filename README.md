# Casino Bonus Scraper

A small technical assessment project that scrapes casino bonus information from a public source, uses a language model to structure free-text bonus terms, saves the results as JSON, and displays the data in a React web page.

## Tech Stack



## Project structure

- `scraper/` — Python scraper and AI processing
- `data/bonuses.json` — generated scraper output
- `web/` — React + Vite frontend

## Requirements

- Python 3
- Node.js and npm
- Gemini API key

## Run the scraper

From the project root:

```bash
cd scraper
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

Create a .env file inside scraper/:

```text
GEMINI_API_KEY=your_api_key_here
```

Run:

```bash
python scraper.py
```

The scraper writes the structured results to:

```json
data/bonuses.json
```

The scraper uses a public casino comparison page and respects the site's robots.txt. It does not bypass login pages, CAPTCHAs, or other access restrictions.

## Run the web app

From the project root:

```bash
cd web
npm install
npm run dev
```

Open the local URL shown by Vite.

### Production build

```bash
npm run build
```

The production files are generated in:

```text
web/dist/
```

## AI usage

Gemini is used to convert free-text bonus terms into structured fields such as the welcome bonus, wagering requirement, and minimum deposit.

## Source

The assessment data is collected from:

`https://betproof.co.za/casino-bonuses-south-africa/`
