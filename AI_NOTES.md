# AI notes

1. Tool used: Google Gemini API (`gemini-3.5-flash-lite`) through the `google-genai` Python package.

2. I used the model to convert free-text casino bonus terms into structured JSON fields.

3. One model result was imperfect: Hollywoodbets was returned as `1x` even though the source contained separate sports and spins wagering terms.

4. I caught this by comparing the generated JSON against the original scraped source table.

5. In production I would add deterministic validation and human review for ambiguous bonus terms rather than relying entirely on the model.
