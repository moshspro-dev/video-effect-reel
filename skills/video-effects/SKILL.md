---
name: video-effects
description: Look up video-editing effects, transitions and looks (whip pan, speed ramp, match cut, VHS, word-by-word captions, split screen, rack focus and about 120 more) with practical recipes before building them in an edit. Use whenever the user asks for an effect, a transition, a look or "something like in that reel", or when you plan transitions, emphasis or captions for a cut.
---

# Video effect recipes

This plugin bundles a library of 123 editing techniques. Each entry says what the effect looks like, when to use it and how to recreate it on the user's **own footage**, often with an FFmpeg command that was test-run. Look recipes up instead of improvising from memory.

## Look it up

Run the bundled search (Python 3 only, no installs). `<skill dir>` is the base directory of this skill, shown when the skill loads. If you can't see it, the plugin lives under `~/.claude/plugins/cache/video-effect-reel/video-effects/<version>/` and the skill is its `skills/video-effects` folder:

```bash
python3 "<skill dir>/../../reel_effects.py" find "speed ramp" --limit 5
```

- Use the user's idea as the query: an effect name (`whip pan`), a goal (`hide a cut`), a category word (`transition`, `blur`, `typography`) or a tool (`ffmpeg`). All words must match.
- `--json` gives structured output. Without a match the command prints "No matches." and exits with 1; try a simpler or related word.
- If the script can't run, read `<skill dir>/../../library/EFFECTS.md` and search it instead.

## Use the recipe

1. Read the recipe and the "when to use" note, then check it fits the shot. Say which recipe you chose and why in one line.
2. Adapt it to the tool the project actually uses (FFmpeg, Remotion, HyperFrames, After Effects or another editor). Recipes are written for general tools, so translate filter names and parameters, and say so when something can't be done with the available tools.
3. Anchor each effect to a specific moment (a word in the transcript, a beat, a cut) and keep it short. One or two well-placed effects beat many.
4. Keep the project's existing style (palette, fonts, caption placement) unless the user says otherwise.
5. Apply recipes to the user's own footage only. Don't copy footage, music or assets from other people's videos.

## Limits

- The recipes are general techniques, not claims that a particular Reel used them.
- Analyzing a new video into recipes needs the full project (FFmpeg, Claude Code and `./setup.sh`). See the project README: https://github.com/moshspro-dev/video-effect-reel
