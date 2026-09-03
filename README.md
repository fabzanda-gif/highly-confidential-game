# Highly Confidential

A two-player asynchronous investigation game set during the Cold War.

Players are rival intelligence officers investigating the same case. They spend
Action Points to interview witnesses, inspect evidence, exchange classified
clues, and submit competing case theories.

## Current status

The repository contains an early Streamlit interface prototype. The current
flow supports:

- agent codename entry;
- creating or joining a match;
- a temporary local waiting-room simulation;
- the opening briefing for the first case.

The lobby is currently stored in Streamlit session state. Real two-device,
asynchronous matches will be added with Supabase.

## Planned features

- Mobile-first Streamlit interface
- Two-player asynchronous matches
- Hand-authored investigation cases
- Shared and private clues
- Action Point system
- Intelligence exchanges
- Random incident cards
- Early accusations and final reports
- Persistent accounts and matches with Supabase
- Optional AI narration with Groq

## First case

### Operation Cold Turkey

Berlin, 1978. A microfilm disappears from a locked diplomatic pouch during a
six-minute blackout at Hotel Europa.

Five suspects were present. Everyone has an explanation. Most of the
explanations are terrible.

## Technology

- Python
- Streamlit
- Supabase — planned for authentication and persistence
- Groq — planned as an optional narrator

## Run locally

1. Clone the repository:

   ```bash
   git clone https://github.com/fabzanda-gif/highly-confidential-game.git
   cd highly-confidential-game
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Activate it on macOS or Linux:

   ```bash
   source .venv/bin/activate
   ```

   On Windows PowerShell:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the application:

   ```bash
   streamlit run app.py
   ```

## Secrets

Never commit API keys. When Supabase and Groq are introduced, local secrets
will be stored in `.streamlit/secrets.toml` and production secrets will be
configured in Streamlit Community Cloud.
