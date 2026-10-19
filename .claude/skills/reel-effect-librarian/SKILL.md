---
name: reel-effect-librarian
description: Analyze reference Reels or videos for editing rhythm and visual effects, then document reusable, evidence-backed techniques in the local effect library. Use for video-style analysis, not for generating replacement footage.
---

# Reel Effect Librarian

For an automated analysis request that includes timestamped contact sheets and a JSON schema, analyze the sheets as consecutive frames from one video. Prioritize short visual effects, transitions, timing, and editing rhythm over plot summary. Preserve the user's footage as the intended source material; explain how to recreate the observed treatment on their own shots.

For every effect, include approximate start/end time, concise description, category, visible frame evidence, confidence (`high`, `medium`, or `low`), and a practical recreation recipe. Distinguish direct visual evidence from uncertain interpretation. Do not infer exact plugin names or claim sound details from silent frames. Report cuts, speed changes, overlays, camera movement, blur, compositing, color, and text only when supported by the frames.

For automated analysis, return exactly one JSON object matching the schema embedded in the request and do not modify files; the local CLI validates the response and stages it for the user to name/approve.

For an interactive request to apply or compare techniques, read the starter library (`library/EFFECTS.md`; `library/effects.json` when details are needed) and the user's private analyses in `local/ANALYSES.md` if it exists, then give practical, evidence-backed suggestions using the user's own footage. Do not claim that the model has been trained or permanently changed. Reuse library entries as references, but do not claim an effect appears in a new video unless it is independently visible there. Do not edit the library unless the user explicitly asks.

The library separates `starter_effects` in `library/effects.json` (general recipes, not observed in a specific Reel) from the user's private `analyses` in `local/analyses.json` (techniques visibly identified in user-provided videos, never committed). When analyzing a new video, compare visible techniques against both groups and report only strong technical matches as same/similar, with the exact catalog ID and a short reason. Similarity is a review suggestion, not a reason to discard the new analysis; the user decides whether it is a duplicate.

Answer in the language the user writes in. For automated analysis, write text values in the language named in the request.

To look up techniques quickly, run `./reel-effects find <words>` (`--json` gives structured output) instead of reading the whole library. It searches the shared recipes and the user's private analyses.
