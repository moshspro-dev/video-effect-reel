# Contributing

Thanks for helping grow the effects library! Contributions are welcome as issues or pull requests.

## Suggest an effect (no code)

Open an issue with the **Effect suggestion** form. Describe what is visible on screen and how to recreate it with your own footage. A link to documentation or a tutorial helps.

## Add an effect with a pull request

1. Add an object to `starter_effects` in `library/effects.json`:

   ```json
   {
     "id": "speed-ramp",
     "name": "Speed ramp",
     "aliases": ["variable speed", "רמפת מהירות"],
     "category": "Timing/Speed",
     "summary": "What is visible on screen, in a sentence or two.",
     "when_to_use": "When the effect fits, and when it doesn't.",
     "recipe": "Practical steps to recreate it on your own footage: timing, values, and an FFmpeg command if there is one.",
     "tags": ["speed-ramp", "rhythm"],
     "reference": "https://ffmpeg.org/ffmpeg-filters.html#setpts_002c-asetpts",
     "he": {
       "category": "קצב/מהירות",
       "summary": "…",
       "when_to_use": "…",
       "recipe": "…"
     }
   }
   ```

   - `id`: unique, lowercase kebab-case.
   - `name`: the English name editors recognize. `aliases` can hold other names in any language; they help search.
   - `category`: reuse an existing category where possible; check the existing ones in `library/EFFECTS.md`.
   - The main fields are in **English**. The `he` block is an optional Hebrew translation. If you include it, `category`, `summary`, `when_to_use` and `recipe` are required, and `name`, `tags` and `reference` are optional overrides. Effects without a `he` block show in English in Hebrew mode. Hebrew speakers are welcome to add missing translations.
   - `reference`: a documentation URL, or `Common editing technique` when there is no single source.
   - Recipes describe how to treat the user's **own footage**. Do not add copyrighted assets, other people's videos or links to them.
   - If the recipe includes an FFmpeg command, run it once to make sure it works.

2. Regenerate the readable indexes (English and Hebrew) and validate:

   ```bash
   ./reel-effects index
   ./reel-effects check
   ```

   `check` also runs automatically on every pull request.

3. Before adding an effect, search the library (`library/EFFECTS.md`) to avoid duplicates. Variants of an existing effect usually belong in that entry's recipe.

## Code changes

- Keep changes focused. Match the existing style: standard library first, minimal dependencies.
- Run `python3 -m py_compile reel_effects.py web_server.py` and `./reel-effects check`.
- Describe how you tested the change in the pull request. For example: a local video run, or the web page on a phone.

## What not to commit

Personal analyses live in the git-ignored `local/` folder and never belong in a pull request. Don't add analyses of other people's videos to the shared library. Never commit `work/`, `local/`, downloaded videos, cookies, API keys or local settings.
