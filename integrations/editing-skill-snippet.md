# Connecting the library to an editing skill or agent

Paste the section below into your editing skill's `SKILL.md` (or into a `style.md` / `CLAUDE.md` in each video project folder).
Replace `/path/to/video-effect-reel` with where you cloned this repository.

The library only documents techniques. The editing tool (HyperFrames, Remotion, FFmpeg…) still does the rendering.

---

## Effect library (video-effect-reel)

A library of editing effects with practical recipes lives at `/path/to/video-effect-reel`. Use it instead of inventing effects from memory.

- **Look up before you build.** When the user asks for an effect, transition, look or "something like in that reel", or when you plan transitions for a first cut, run:
  `/path/to/video-effect-reel/reel-effects find <words>`
  English and Hebrew words both work (`find "speed ramp"`, `find רמפת מהירות`). Add `--lang he` for Hebrew output, `--limit 3` for fewer results, `--json` for structured output. Results include the user's private analyses of reels they studied.
- **Read the recipe, then adapt it.** Recipes are written for general tools (FFmpeg filters, Remotion, After Effects terms). Translate them into the project's engine, keep the project's style defaults (palette, fonts, subtitle placement), and say so when a recipe cannot be done with the available tools.
- **Anchor to a moment.** Place each effect on a word or beat from the word-level transcript, and keep it short and sparing.
- **Existing references win for what they cover.** If the skill's own `references/effects.md` already has a recipe for an effect, use that one; use the library for everything else.
- **Rights.** Recipes apply to the user's own footage. Never reuse footage, music or assets from the reels that were analyzed; they are inspiration only.
- **Learning from a new reel.** Don't download links from the shell. Ask the user to save the video to the folder and run `/path/to/video-effect-reel/reel-effects add <file>` (or use the library's web page); afterwards `find` includes the new analysis.
- **Language.** `reel-effects lang he|en` sets the library's language for the web page and for new analyses; `find --lang` overrides it per call.
