# AlignAI Prompt Hub

Static site for prompts.alignai.business — AI prompts optimized for small business.

## Local dev
1. Copy `.env.example` to `.env` and fill in Supabase credentials
2. `pip install -r requirements.txt`
3. `python3 build.py`
4. Open `dist/index.html`

## Deploy
Automatic via GitHub Actions on push to main or daily at 5AM UTC.
Manual trigger available via Actions tab.
