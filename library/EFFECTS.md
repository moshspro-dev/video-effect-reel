# Effect Library

Starter recipes: 123  
Other languages: [עברית](EFFECTS.he.md)

General reusable techniques, not claims that these appeared in an analyzed video.

### Whip pan with motion blur — Transition

A fast horizontal or vertical camera move that links two shots; the motion blur hides the cut.

When to use: When there is movement or an energy change on the beat, ideally when the shots can continue in the same direction.

Recipe: Using the original shots: end the first with a fast swish, cut while the frame is blurred, and start the next in the same direction. Add a short motion blur and settle the frame right after the cut. Time the cut to the beat.

Tags: transition, motion-blur, rhythm, own-footage  
Reference: https://www.remotion.dev/docs/transitions/

### Zoom-blur / punch-in — Camera motion

A fast push in or out, sometimes with blur, to emphasize a moment or to transition between shots.

When to use: To emphasize a detail, a reaction or a musical moment; keep the point of interest inside the frame.

Recipe: On the original shot, create a fast scale with a short ease toward the point of interest and back, or into a cut. Add blur only at the peak of the move and remove it right away. Do not replace or generate footage.

Tags: zoom, blur, emphasis, own-footage  
Reference: https://www.remotion.dev/docs/transitions/

### Flash-frame cut — Transition

A very short flash between two shots, usually synced to a musical hit.

When to use: For a sharp transition or to emphasize a hit; used too often it can feel harsh.

Recipe: Cut between the shots on the beat and add a white/exposure layer for one to a few frames with a short fade. Keep the details of both shots visible before and after.

Tags: flash, transition, beat-sync  
Reference: https://www.remotion.dev/docs/transitions/

### Film-burn / light leak — Light overlay

A flicker of light or colored burn that appears over the image, used as a transition or a short texture.

When to use: For a soft transition or an analog feel; avoid covering the key moment of action.

Recipe: Keep the original shot and blend a short light-leak/film-burn layer over it in screen/add mode with animated opacity. Sync the peak to the cut or the beat.

Tags: film, light-leak, overlay, transition  
Reference: https://www.remotion.dev/docs/transitions/

### Wipe / mask reveal — Transition

The next shot is revealed by a mask that moves across or down the frame, or follows a shape.

When to use: When there is a line, movement or shape in the frame that can carry into the next shot.

Recipe: Animate a mask across the original shot sitting above the next shot. Aim the mask edge in the direction of body or camera movement and finish the reveal on the beat.

Tags: wipe, mask, transition  
Reference: https://www.remotion.dev/docs/transitions/

### Speed ramp — Timing/Speed

A gradual speed change within a shot: slowing down for a key moment and then speeding up, or the reverse.

When to use: On action with clear movement, when the slowdown emphasizes a moment without hurting readability.

Recipe: Mark the action point in the original shot, plan speed changes with a smooth curve around it, and keep the motion continuous. Check the audio; if sync can't be kept, detach the source audio and use a licensed soundtrack or sound effect that was provided.

Tags: speed-ramp, slow-motion, rhythm  
Reference: https://ffmpeg.org/ffmpeg-filters.html#setpts_002c-asetpts

### RGB split / chromatic glitch — Color distortion

A slight, separate offset of the RGB channels at the edges, sometimes as a short pulse with frame shake.

When to use: For a brief moment of tension, energy or glitch; don't keep it strong for the whole video.

Recipe: Apply a subtle color-channel offset to the original shot for a few frames, intensify it at the peak and return to normal. A short jitter can be added, but don't hide the footage.

Tags: RGB, glitch, color, own-footage  
Reference: https://ffmpeg.org/ffmpeg-filters.html#chromashift

### Freeze frame with punch-in — Emphasis

A short hold on a chosen frame, sometimes with scale, outline or a caption, then back to motion.

When to use: On a reaction, pose or reveal that still reads when the motion stops.

Recipe: Freeze an existing frame from the original shot for a few frames, add a small punch-in or a short caption if needed, then continue or cut back into the motion on the beat.

Tags: freeze-frame, emphasis, beat-sync  
Reference: Common editing technique

### Camera shake on hit — Camera motion

A short, controlled shift/rotation around a hit, landing or beat, with a fast decay.

When to use: When the action in frame justifies a sense of impact; don't add it to every cut.

Recipe: On the original shot, add short non-periodic position/rotation offsets around the hit, decaying within a few frames. Check that the edges don't reveal empty areas.

Tags: shake, impact, beat-sync  
Reference: Common editing technique

### Kinetic text hit — Typography

Words or labels enter with a short, punchy motion synced to the voice-over or beat.

When to use: When there is a short message the user provided or approved; don't invent facts or text.

Recipe: Add text as an overlay above the original video with a fast entrance (slide/pop), a readable hold and a clean exit. Sync to the syllable or beat and keep safe margins for a vertical screen.

Tags: text, typography, beat-sync, overlay  
Reference: https://www.remotion.dev/docs/transitions/

### Cross dissolve — Transition

A soft overlapping fade between two shots

When to use: A calm, unobtrusive transition

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a calm, unobtrusive transition.

Tags: transition, own-footage  
Reference: https://www.remotion.dev/docs/transitions/presentations/

### Fade through black — Transition

The shot fades to black and the next one opens from it

When to use: To mark a pause or a scene change

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: to mark a pause or a scene change.

Tags: transition, own-footage  
Reference: https://www.remotion.dev/docs/transitions/presentations/

### Fade through white — Transition

A white fade/flash that reveals the next shot

When to use: A bright or energetic transition

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a bright or energetic transition.

Tags: transition, own-footage  
Reference: https://www.remotion.dev/docs/transitions/presentations/

### Fade through color — Transition

A transition through a chosen intermediate color

When to use: To connect shots within a specific color palette

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: to connect shots within a specific color palette.

Tags: transition, own-footage  
Reference: https://www.remotion.dev/docs/transitions/presentations/

### Push cut — Transition

The next shot pushes the previous one out with a short flash

When to use: A musical hit or an emphasized entrance

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a musical hit or an emphasized entrance.

Tags: transition, own-footage  
Reference: https://www.remotion.dev/docs/transitions/presentations/

### Directional slides — Transition

The next shot slides in horizontally or vertically

When to use: Match the direction of motion and the format

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: match the direction of motion and the format.

Tags: transition, own-footage  
Reference: https://www.remotion.dev/docs/transitions/presentations/

### Smooth slide — Transition

A slide with a soft/blurred edge

When to use: When a hard slide feels stiff

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: when a hard slide feels stiff.

Tags: transition, own-footage  
Reference: https://www.remotion.dev/docs/transitions/presentations/

### Directional/diagonal wipe — Transition

A mask reveals the next shot horizontally, vertically or diagonally

When to use: To continue a line or movement from the frame

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: to continue a line or movement from the frame.

Tags: transition, own-footage  
Reference: https://www.remotion.dev/docs/transitions/presentations/

### Iris / circle reveal — Transition

A circular mask opens or closes around a point

When to use: To direct attention to a detail

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: to direct attention to a detail.

Tags: transition, own-footage  
Reference: https://www.remotion.dev/docs/transitions/presentations/

### Clock wipe — Transition

A radial reveal that sweeps like a clock hand

When to use: A graphic or timer-style transition

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a graphic or timer-style transition.

Tags: transition, own-footage  
Reference: https://www.remotion.dev/docs/transitions/presentations/

### Flip transition — Transition

The shot flips around an axis like a card

When to use: A playful, deliberate transition

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a playful, deliberate transition.

Tags: transition, own-footage  
Reference: https://www.remotion.dev/docs/transitions/presentations/

### Zoom in/out transition — Transition

The outgoing shot zooms in and the incoming one zooms out, or the reverse

When to use: To connect shots with inward/outward motion

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: to connect shots with inward/outward motion.

Tags: transition, own-footage  
Reference: https://www.remotion.dev/docs/transitions/presentations/

### Dreamy zoom — Transition

A zoom with a gentle rotation and a white flash

When to use: A dreamy, music-video transition

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a dreamy, music-video transition.

Tags: transition, own-footage  
Reference: https://www.remotion.dev/docs/transitions/presentations/

### Directional blur transition — Transition

Motion blur in the direction of the transition

When to use: To add speed to a slide or whip

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: to add speed to a slide or whip.

Tags: transition, own-footage  
Reference: https://www.remotion.dev/docs/transitions/presentations/

### Book/page flip — Transition

A page-turn style swap

When to use: Storytelling or an album feel

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: storytelling or an album feel.

Tags: transition, own-footage  
Reference: https://www.remotion.dev/docs/transitions/presentations/

### Glow dissolve — Transition

A dissolve with a glowing edge between the shots

When to use: A luminous look

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a luminous look.

Tags: transition, own-footage  
Reference: https://www.remotion.dev/docs/transitions/presentations/

### Ripple distortion — Transition

A ripple distortion that advances during the transition

When to use: Water, dreams or deliberate distortion

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: water, dreams or deliberate distortion.

Tags: transition, own-footage  
Reference: https://www.remotion.dev/docs/transitions/presentations/

### Crosswarp — Transition

Both shots stretch and warp up to the cut

When to use: A fast, dynamic transition

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a fast, dynamic transition.

Tags: transition, own-footage  
Reference: https://www.remotion.dev/docs/transitions/presentations/

### Crosszoom — Transition

Both shots move through the center with zoom/blur

When to use: A strong beat or a scene change

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a strong beat or a scene change.

Tags: transition, own-footage  
Reference: https://www.remotion.dev/docs/transitions/presentations/

### Perspective swap — Transition

A swap with perspective/reflection

When to use: A stylized 3D transition

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a stylized 3D transition.

Tags: transition, own-footage  
Reference: https://www.remotion.dev/docs/transitions/presentations/

### Blur slide — Transition

Both shots slide with motion blur

When to use: A fast whip

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a fast whip.

Tags: transition, own-footage  
Reference: https://www.remotion.dev/docs/transitions/presentations/

### Cube rotate — Transition

The shots rotate like the faces of a cube

When to use: A bold effect, not a default

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a bold effect, not a default.

Tags: transition, own-footage  
Reference: https://www.remotion.dev/docs/transitions/presentations/

### FFmpeg xfade families — Transition

FFmpeg includes fade, wipes in eight directions, slides, circles, diagonals, slices, squeeze, dissolve, pixelize, blur and radial

When to use: Pick a variant to match the motion; the two shots need to overlap

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: pick a variant to match the motion; the two shots need to overlap.

Tags: transition, own-footage  
Reference: https://ffmpeg.org/ffmpeg-filters.html

### Brightness pulse — Color/Exposure

A short brightness pulse and back to the original exposure

When to use: Syncing to the beat

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: syncing to the beat.

Tags: color-exposure, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Contrast hit — Color/Exposure

A momentary jump in contrast

When to use: Emphasizing a hit or cut

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: emphasizing a hit or cut.

Tags: color-exposure, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Color correction — Color/Exposure

Correcting exposure, contrast, saturation and temperature

When to use: Matching color between shots

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: matching color between shots.

Tags: color-exposure, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Exposure ramp — Color/Exposure

A gradual or pulsed exposure change

When to use: A bright entrance or exit

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a bright entrance or exit.

Tags: color-exposure, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Selective monochrome — Color/Exposure

A brief switch to black-and-white or a single color

When to use: Dramatic emphasis

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: dramatic emphasis.

Tags: color-exposure, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Hue shift — Color/Exposure

A gradual or brief hue rotation

When to use: A glitch or a colorful change

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a glitch or a colorful change.

Tags: color-exposure, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Invert / negative flash — Color/Exposure

A momentary color inversion

When to use: A short glitch

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a short glitch.

Tags: color-exposure, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Levels/gamma — Color/Exposure

Control over black point, white point and gamma

When to use: Tonal adjustment

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: tonal adjustment.

Tags: color-exposure, own-footage  
Reference: https://www.remotion.dev/docs/effects

### LUT look — Color/Exposure

Overall color mapping with a LUT

When to use: A consistent look after base correction

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a consistent look after base correction.

Tags: color-exposure, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Saturation pulse — Color/Exposure

Briefly boosting or reducing saturation

When to use: Emphasizing a beat or a transition

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: emphasizing a beat or a transition.

Tags: color-exposure, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Shadows/highlights — Color/Exposure

Adjusting detail in dark and bright areas

When to use: Recovering detail in a high-contrast shot

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: recovering detail in a high-contrast shot.

Tags: color-exposure, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Duotone — Color/Exposure

Mapping shadows and highlights to two colors

When to use: A graphic look on footage

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a graphic look on footage.

Tags: color-exposure, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Color tint — Color/Exposure

A controlled bias toward one color

When to use: Matching a color palette

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: matching a color palette.

Tags: color-exposure, own-footage  
Reference: https://www.remotion.dev/docs/effects

### White balance shift — Color/Exposure

Correcting or shifting warmth/coolness and tint

When to use: Fixing lighting or a warm/cool shift

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: fixing lighting or a warm/cool shift.

Tags: color-exposure, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Vibrance — Color/Exposure

Selectively boosting muted colors

When to use: Adding life without oversaturation

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: adding life without oversaturation.

Tags: color-exposure, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Thermal/heat map — Color/Exposure

Thermal-style color mapping on the shot

When to use: A graphic or experimental moment

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a graphic or experimental moment.

Tags: color-exposure, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Gaussian blur — Blur/Glow

A soft blur with controlled strength

When to use: Softening or a transition

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: softening or a transition.

Tags: blur-glow, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Progressive blur — Blur/Glow

Blur that varies along a gradient

When to use: Keeping one area in focus

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: keeping one area in focus.

Tags: blur-glow, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Radial progressive blur — Blur/Glow

Blur around a point or ellipse

When to use: Focus or a sense of zoom

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: focus or a sense of zoom.

Tags: blur-glow, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Region blur — Blur/Glow

Blurring a chosen region only

When to use: Hiding something or focusing attention

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: hiding something or focusing attention.

Tags: blur-glow, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Drop shadow — Blur/Glow

A soft shadow beneath an isolated element or text

When to use: Overlays or cutouts

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: overlays or cutouts.

Tags: blur-glow, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Glow / soft halo — Blur/Glow

A soft halo around highlights

When to use: Dreamy lighting

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: dreamy lighting.

Tags: blur-glow, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Outline / edge stroke — Blur/Glow

A stroke around a mask or element

When to use: Text or an isolated object

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: text or an isolated object.

Tags: blur-glow, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Light trail — Blur/Glow

A light/motion trail in a given direction

When to use: Fast movement

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: fast movement.

Tags: blur-glow, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Evolve directional reveal — Reveal/Mask

A progressive mask reveals a layer in a given direction

When to use: Revealing text or the next shot

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: revealing text or the next shot.

Tags: reveal-mask, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Tear reveal — Reveal/Mask

A torn edge reveals the layer underneath

When to use: A paper/editorial transition

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a paper/editorial transition.

Tags: reveal-mask, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Venetian blinds — Reveal/Mask

A reveal in parallel stripes

When to use: A short graphic transition

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a short graphic transition.

Tags: reveal-mask, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Mirror reflection — Transform/Distort

Horizontal or vertical mirroring of the shot

When to use: Symmetry or a change of direction

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: symmetry or a change of direction.

Tags: transform-distort, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Animated scale/position — Transform/Distort

Animating scale/position on the original shot

When to use: A punch-in or Ken Burns move

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a punch-in or Ken Burns move.

Tags: transform-distort, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Tile/repeat — Transform/Distort

Tiling/repeating the source frame

When to use: A stylized glitch

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a stylized glitch.

Tags: transform-distort, own-footage  
Reference: https://www.remotion.dev/docs/effects

### XY pixel translate — Transform/Distort

Pixel offsets along the axes

When to use: Jitter or glitch

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: jitter or glitch.

Tags: transform-distort, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Barrel distortion — Transform/Distort

Wide-lens barrel distortion

When to use: POV or action

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: POV or action.

Tags: transform-distort, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Chromatic aberration — Transform/Distort

A small RGB offset, mostly at the edges

When to use: A short glitch

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a short glitch.

Tags: transform-distort, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Fisheye — Transform/Distort

Wide-angle/fisheye lens distortion

When to use: POV or action

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: POV or action.

Tags: transform-distort, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Corner pin/screen replace — Transform/Distort

Fitting the corners to a plane in perspective

When to use: Pinning onto an existing screen or sign

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: pinning onto an existing screen or sign.

Tags: transform-distort, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Wave distortion — Transform/Distort

A sinusoidal wave distortion

When to use: Water or dreams

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: water or dreams.

Tags: transform-distort, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Skew/shear — Transform/Distort

Shearing the frame on one or two axes

When to use: A motion accent

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a motion accent.

Tags: transform-distort, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Film grain/noise — Texture/Stylize

Subtle grain over the footage

When to use: An analog look

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: an analog look.

Tags: texture-stylize, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Halftone — Texture/Stylize

Converting tones into print dots

When to use: Comic or pop-art

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: comic or pop-art.

Tags: texture-stylize, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Dot grid — Texture/Stylize

A dot mask based on the source colors

When to use: A graphic layer

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a graphic layer.

Tags: texture-stylize, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Paper texture — Texture/Stylize

A paper texture over the footage

When to use: Editorial or collage

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: editorial or collage.

Tags: texture-stylize, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Emboss — Texture/Stylize

A relief-like edge emboss

When to use: A graphic moment

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a graphic moment.

Tags: texture-stylize, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Scanlines — Texture/Stylize

Horizontal CRT-style lines

When to use: Retro or glitch

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: retro or glitch.

Tags: texture-stylize, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Noise displacement — Texture/Stylize

Local distortion driven by noise

When to use: A short glitch

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a short glitch.

Tags: texture-stylize, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Pixel dissolve — Texture/Stylize

Gradual breakup/appearance in pixels

When to use: A digital transition

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a digital transition.

Tags: texture-stylize, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Pixelate — Texture/Stylize

Enlarged pixels / a low-res look

When to use: Glitch or stylized hiding

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: glitch or stylized hiding.

Tags: texture-stylize, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Vignette — Texture/Stylize

Moderate darkening of the edges

When to use: Focus on the center

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: focus on the center.

Tags: texture-stylize, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Shine sweep — Texture/Stylize

A glossy highlight sweeps across an object or text

When to use: A filmed product or logo, with a mask

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a filmed product or logo, with a mask.

Tags: texture-stylize, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Roughen edges — Texture/Stylize

Rough, organic mask edges

When to use: Cutouts or paper looks

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: cutouts or paper looks.

Tags: texture-stylize, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Speckle/dust — Texture/Stylize

Dust or small specks over the image

When to use: A subtle film texture

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a subtle film texture.

Tags: texture-stylize, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Shrinkwrap/plastic sheen — Texture/Stylize

A plastic highlight and distortion around shapes

When to use: An experimental look

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: an experimental look.

Tags: texture-stylize, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Starburst rays — Texture/Stylize

Rays around a point of light

When to use: A glowing or comic moment

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a glowing or comic moment.

Tags: texture-stylize, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Procedural light leak — Texture/Stylize

A colored light leak as an overlay

When to use: A transition or an analog look

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: a transition or an analog look.

Tags: texture-stylize, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Color key/greenscreen — Compositing/Mask

Removing a key color to reveal another layer

When to use: Only with an even background and a clean mask

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: only with an even background and a clean mask.

Tags: compositing-mask, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Motion blur — Blur/Glow

Motion blur from a trail of frames

When to use: Whips and fast movement

Recipe: Apply it to the pixels of the original shot only; don't replace or generate footage. Keep the time range short, animate the parameter smoothly, and ease it back to zero at the end so the image stays readable. Typical use: whips and fast movement.

Tags: blur-glow, own-footage  
Reference: https://www.remotion.dev/docs/effects

### Match cut — Transition

A cut between two shots where a shape, position or movement lines up in the frame, so the eye carries on even though the place or time has changed.

When to use: When two shots share a similar object or motion (a hand closing a door, a ball, a face in the center); great for before/after and for jumping between locations.

Recipe: Mark the frame in shot A where the object sits at a given position and size, and find a matching frame in shot B. Align B with scale/position so the object lands in exactly the same spot (check with a 50% opacity overlay), and cut in the middle of the motion, not at its end. Add 2–4 frames of motion blur or a flash to hide small differences.

Tags: transition, match-cut, continuity, own-footage  
Reference: Common editing technique

### Punch-in jump cut — Transition

A cut within the same talking-head shot that alternates the framing between 100% and about 115–130%, to hide removed pauses and add energy — no blur.

When to use: In talking videos after cutting pauses or mistakes, and to emphasize a key sentence.

Recipe: At each cut, alternate between the wide framing and an enlarged crop (e.g. crop=iw/1.2:ih/1.2, then scale back to the original resolution) while the face stays in the same relative position. Don't go beyond about 130% on 1080p footage to keep it sharp. Change size only at cuts, not mid-sentence; a smooth 3–5 frame punch-in on a key word also works.

Tags: transition, jump-cut, talking-head, zoom, own-footage  
Reference: https://ffmpeg.org/ffmpeg-filters.html#crop

### Smash cut — Transition

An abrupt cut between two shots with opposite energy (quiet→loud, slow→fast) and no transition, to create surprise or a comic punch.

When to use: For a punchline, a reaction, or the jump from build-up to peak; it only works when the contrast is sharp.

Recipe: Trim the first shot right before the 'answer' and cut straight to a shot with strong contrast in color, size or motion. No fade. Place the cut exactly on the beat or the start of the word; a single black frame before the cut can strengthen the hit.

Tags: transition, hard-cut, rhythm, beat-sync  
Reference: Common editing technique

### Object/body wipe — Transition

An object close to the camera (a body, a pillar, a hand, a car) crosses the frame, and the next shot is revealed behind it while it covers the screen.

When to use: When a foreground object naturally crosses the frame; great for street footage and moving between locations.

Recipe: Find an object passing in front of the camera in shot A. Draw a mask that follows its leading edge (keyframes every 1–2 frames, slight feather) and place shot B under A, so B is revealed where the object has already passed. If the object covers the whole frame for even one frame, a plain cut on that frame is enough. Shot B should ideally continue in the same direction of motion.

Tags: transition, mask, rotoscope, own-footage  
Reference: Common editing technique

### Zoom-through transition — Transition

A fast zoom into a dark area or object in the shot (an eye, an opening, a screen, a cup), and the next shot starts from inside that area.

When to use: When the shot has an area that can act as a 'portal' — a phone screen, a door, a pupil, the sky.

Recipe: Animate the scale of shot A (ease-in, 6–10 frames) toward the object so it stays centered. Mask the object (or rely on it being dark) and place shot B behind it, small, growing with the zoom until it fills the frame. Add a short zoom blur at the peak and an ease-out at the start of B.

Tags: transition, zoom, mask, own-footage  
Reference: Common editing technique

### Spin transition — Transition

The shot spins fast by 90°–360° with motion blur, and at the peak of the spin it switches to the next shot, which continues in the same direction.

When to use: In energetic montages, travel and fast music; less suited to talking content.

Recipe: Scale both shots to about 140% so the corners aren't revealed while spinning (or use mirror edges). Animate rotation at the end of A and the start of B (ease-in for A, ease-out for B, 8–12 frames in total) and cut when the spin is fastest. Add motion/radial blur proportional to the speed. In FFmpeg, use rotate with a time expression followed by crop.

Tags: transition, rotation, motion-blur, own-footage  
Reference: https://ffmpeg.org/ffmpeg-filters.html#rotate

### Infinite zoom — Transition

A continuous zoom into the frame where each shot contains the next one at its center, so the camera seems to dive forever.

When to use: In a montage of several places or stages, or with images that can nest inside each other.

Recipe: Arrange shots so the center of each can contain the next. Place B small (e.g. 20%) in the center of A with a soft mask, and animate an exponential scale on both layers together (a constant zoom rate on a logarithmic scale) until B fills the screen, then repeat with the next shot. Match color between layers so the edge doesn't stand out.

Tags: transition, zoom, loop, own-footage  
Reference: Common editing technique

### Reverse / rewind — Timing/Speed

Footage played backwards — sometimes fast, as a 'rewind' — to create an impossible action or go back to an earlier moment.

When to use: For physical actions that look surprising in reverse (water, a throw, a jump) and for a 'going back' beat in a story.

Recipe: Trim a short segment (ideally up to about 10 seconds, since FFmpeg's reverse keeps the whole segment in memory) and apply trim then reverse. For a rewind effect, speed it up with setpts=PTS/3 and add light scanlines or RGB split. Audio: areverse or mute.

Tags: reverse, time, rhythm, own-footage  
Reference: https://ffmpeg.org/ffmpeg-filters.html#reverse

### Boomerang / ping-pong loop — Timing/Speed

A one-to-two second clip that plays forward and backward in a loop, like an Instagram Boomerang.

When to use: For a short, clear motion — a jump, raising a glass, hair in the wind — and for an opening or ending that holds attention.

Recipe: Trim 0.7–1.5 seconds, duplicate it with reverse and join forward+backward (split → reverse → concat), repeating 2–3 times. Speed it up 1.5–2× so it feels alive, and drop the duplicated frame at the turnaround so there's no visible pause.

Tags: loop, reverse, rhythm, own-footage  
Reference: https://ffmpeg.org/ffmpeg-filters.html#reverse

### Optical-flow slow motion — Timing/Speed

Slowing down footage shot at 24–30 fps while generating in-between frames, so the motion looks smooth instead of choppy.

When to use: When you need a 2–4× slowdown and didn't shoot at a high frame rate; works best with a simple background and no crossing objects.

Recipe: Slow down with setpts=2*PTS (or more), then minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:vsbmc=1 to generate in-between frames. Check edges for artifacts (hands, hair, crossing objects) and shorten the segment if there's smearing. If you shot at 60/120 fps, just play it back at 30 fps without interpolation.

Tags: slow-motion, interpolation, rhythm, own-footage  
Reference: https://ffmpeg.org/ffmpeg-filters.html#minterpolate

### Stutter / frame repeat — Timing/Speed

A quick repeat of 3–6 frames two or three times, creating a rhythmic stutter synced to the beat.

When to use: On a hi-hat or snare in electronic music, and to emphasize a movement or reaction.

Recipe: At the beat, take 3–6 frames and repeat them 2–3 times (e.g. loop=loop=2:size=4:start=<frame number>), then continue normally. You can add a small punch-in or RGB offset on each repeat. Use sparingly — 1–3 times per video.

Tags: stutter, beat-sync, glitch, own-footage  
Reference: https://ffmpeg.org/ffmpeg-filters.html#loop

### Choppy frame rate / stop-motion feel — Timing/Speed

Deliberately dropping the frame rate to 6–12 fps in a section, so motion looks jumpy like stop-motion or animation.

When to use: When switching to an illustrated style, on fast motion, or as a contrast before returning to smooth motion.

Recipe: On the segment, apply fps=8 followed by fps=30 — the file stays 30 fps but each frame is held about 4 times and motion looks choppy. Combine with high contrast or grain, and return to the full frame rate on the next beat.

Tags: frame-rate, stop-motion, stylize, own-footage  
Reference: https://ffmpeg.org/ffmpeg-filters.html#fps-1

### Timelapse / hyperlapse — Timing/Speed

Compressing minutes or hours into a few seconds; in a hyperlapse the camera also travels along a path.

When to use: To show a process (cooking, building, a sunset) or a quick change of place.

Recipe: Speed up 8–60× with setpts=PTS/<factor> (or framestep to skip frames) and drop the audio. For a hyperlapse, stabilize first (vidstabdetect/vidstabtransform if your build has them) and only then speed up; a light tmix smooths jumps. You can add a speed ramp back to normal speed at the key moment.

Tags: timelapse, speed, rhythm, own-footage  
Reference: https://ffmpeg.org/ffmpeg-filters.html#setpts_002c-asetpts

### Beat-synced montage — Timing/Speed

A sequence of short shots where every cut lands on a beat in the music, often getting shorter toward the peak.

When to use: For openings, trip or event recaps; needs enough varied shots.

Recipe: Mark the beats (BPM markers or by hand), trim each shot so it starts on a beat, and shorten shot lengths gradually (e.g. 4→2→1 beats) toward the peak. In each shot pick the moment with the clearest motion, and add an occasional flash or shake on a strong beat. Check that cuts are in sync within ±1 frame.

Tags: beat-sync, montage, rhythm, own-footage  
Reference: Common editing technique

### Echo / ghost trails — Blur/Glow

Previous frames linger semi-transparently behind the moving subject, creating a trail of 'ghosts' or a motion smear.

When to use: For dance, sports and motion against a steady background; less good when the camera moves, since the whole frame smears.

Recipe: For a soft trail: tmix=frames=5 (an average of neighboring frames). For a bright trail that fades slowly: lagfun=decay=0.9 (works well on a bright subject against a dark background). Apply only to a short segment or mask it to the subject, and return to a sharp image after the beat.

Tags: echo, trails, motion, own-footage  
Reference: https://ffmpeg.org/ffmpeg-filters.html#tmix

### Ken Burns pan & zoom — Camera motion

A slow zoom and/or pan across a still image or static shot to bring movement into it.

When to use: For photos, screenshots and static shots inside a sequence that has motion.

Recipe: Start from an image with a higher resolution than the output and use zoompan (e.g. z='min(zoom+0.0015,1.3)':d=<frames> with x/y aimed at the point of interest) or a scale+position animation with easing. Zoom 5–15% over a 3–5 second shot, ending on the important subject. To avoid jitter, upscale the image first (scale=4000:-1) and then apply zoompan.

Tags: camera, zoom, pan, photos  
Reference: https://ffmpeg.org/ffmpeg-filters.html#zoompan

### Dolly zoom (vertigo) — Camera motion

The subject stays the same size in frame while the background expands or shrinks around it — a sense of vertigo or sudden realization.

When to use: For a dramatic or comic moment of realization; needs to be planned when shooting.

Recipe: Shoot while the camera moves toward (or away from) the subject in a straight line at a constant speed, with a wide lens. In the edit, animate scale opposite to the move so the subject's size stays constant (keyframe by face width), cropping to the final frame. Alternative: optical zoom during the move. Stabilize on the subject so it doesn't wobble.

Tags: camera, zoom, perspective, own-footage  
Reference: Common editing technique

### Handheld drift / camera wiggle — Camera motion

Gentle, random movement of the frame that mimics a handheld camera, so a static shot or photo doesn't look frozen.

When to use: On tripod shots, screenshots and photos inside a dynamic video — at very low intensity.

Recipe: Scale the shot up 4–6% and animate position/rotation with slow noise (0.5–1.5 Hz, 5–15 px amplitude, up to 0.5° rotation). In FFmpeg: a small scale, then crop with x/y driven by sin/cos of t at frequencies that aren't multiples of each other. Unlike shake on impact, the movement here is continuous and gentle.

Tags: camera, handheld, wiggle, own-footage  
Reference: https://ffmpeg.org/ffmpeg-filters.html#crop

### Rack focus (simulated) — Camera motion

A focus shift from a near object to a far one (or the reverse) that steers the eye to a new subject.

When to use: When the frame has two layers of depth; best done in camera, but it can be simulated in the edit.

Recipe: In camera: pull focus manually while recording. Simulated: mask the foreground and background and animate opposite gaussian blurs (foreground 0→8 px, background 8→0 px) over 10–20 frames with easing. A 1–2% scale change ('lens breathing') adds realism.

Tags: camera, focus, blur, own-footage  
Reference: Common editing technique

### 2.5D parallax photo — Camera motion

A still image is split into layers (subject and background) and each layer moves at a different speed, creating a sense of depth.

When to use: For archive photos, product shots and opening images; works well with a clear subject.

Recipe: Separate the subject (mask / background removal) and fill in the background behind it (clone/fill) so there's no hole. Animate the background from 100% to 105% scale and the subject from 100% to 112% (or move them in opposite directions) over 3–5 seconds with easing. A light blur on the background and a foreground particle layer deepen the effect.

Tags: camera, parallax, mask, photos  
Reference: Common editing technique

### Split screen / grid — Compositing/Mask

Two or more shots shown at once in a split of the screen — side by side, stacked, or in a grid.

When to use: For comparisons (before/after, two angles), a reaction next to the source, or a fast 'day in the life'.

Recipe: In a vertical 1080×1920 format, usually split into two 1080×960 panes stacked vertically (vstack) or a 2×2 grid (xstack). Crop each shot to fit its pane, keep the subject centered, and add a thin divider or gap. Panes can come in one after another on beats.

Tags: split-screen, compositing, layout, own-footage  
Reference: https://ffmpeg.org/ffmpeg-filters.html#xstack-1

### Picture-in-picture — Compositing/Mask

A small video (e.g. the speaker's face) in a corner, over a main video (a screen, a product, a reaction clip).

When to use: In reaction videos, screen tutorials and product reviews.

Recipe: Shrink the top layer to 30–40% of the frame width, add rounded corners or a border and a shadow, and place it in the safe area (not at the bottom, where Reels captions and icons sit), e.g. overlay=x=W-w-40:y=200. Animate the entrance (scale pop) and don't move the window mid-sentence.

Tags: pip, overlay, compositing, own-footage  
Reference: https://ffmpeg.org/ffmpeg-filters.html#overlay-1

### Text behind subject — Compositing/Mask

A large title placed between the background and the subject, so the subject hides part of the letters and creates depth.

When to use: For an opening, a chapter title or a topic name; needs a clean subject mask.

Recipe: Create a subject mask (segmentation or rotoscoping; with a locked-off camera a few keyframes are enough). Layer order: original video → text → a copy of the subject only, cut out by the mask. Pick a bold, large font in a color that contrasts with the background, positioned so the head and shoulders cover 10–30% of the letters. Animate the text in (scale/fade) once the subject is in place.

Tags: text, mask, depth, compositing, own-footage  
Reference: Common editing technique

### Clone / multiplicity — Compositing/Mask

The same person appears several times in the same frame, as if talking to themselves.

When to use: For comedy sketches, an inner argument and 'types of people' formats.

Recipe: Shoot from a tripod with exposure, focus and white balance locked, recording several takes where the person is in a different part of the frame each time and doesn't cross the seam. In the edit, stack the takes and use a mask with a wide feather along a line with no movement. If the light changed between takes, correct levels/WB per layer so the seam doesn't show.

Tags: clone, mask, compositing, own-footage  
Reference: Common editing technique

### Subject cutout sticker — Emphasis

The subject is cut out from the background, gets a thick white outline and a shadow, and 'pops' out like a sticker — usually on a frozen frame.

When to use: To introduce a person or product, for a 'who's this?' moment or to emphasize a reaction; pairs well with a freeze frame.

Recipe: Pick a frame, separate the subject (background removal), and create an 8–20 px white outline by dilating the alpha channel, plus a soft shadow. Animate scale from 100% to 110% with overshoot and a slight rotation (about 3°), and dim or blur the background. Hold for 0.5–1.5 seconds, then return to the video.

Tags: cutout, outline, freeze-frame, emphasis  
Reference: Common editing technique

### Callouts / animated annotations — Emphasis

Arrows, circles, underlines or boxes drawn on in motion to direct the eye to a detail in the frame.

When to use: In screen tutorials, product reviews and to highlight a small detail viewers might miss.

Recipe: Draw a shape (circle, arrow, line) and animate its stroke from 0% to 100% over 8–12 frames, in a contrasting color, 6–12 px thick. If the object moves, attach the shape to tracking. Add a slight zoom into the marked area, and remove the annotation once the point is made.

Tags: annotation, arrow, highlight, overlay  
Reference: Common editing technique

### Cinematic letterbox bars — Reveal/Mask

Black bars at the top and bottom slide in and narrow the frame to a wide ratio — a 'now it's cinematic' feel.

When to use: For a dramatic moment, a trailer or B-roll; less suited to an entire vertical Reel.

Recipe: Add two black rectangles (drawbox) whose height animates from 0 to the target over 10–15 frames with an ease-out. On 1080×1920 a 2.39:1 ratio leaves only a ~452 px band, so narrower bars are usually used. Check that the subject and captions aren't cut off.

Tags: letterbox, cinematic, overlay, own-footage  
Reference: https://ffmpeg.org/ffmpeg-filters.html#drawbox

### Before/after slider — Reveal/Mask

A divider line moves across the screen and reveals the 'after' version over the 'before', usually with a handle or labels.

When to use: To show an improvement — color grading, a renovation, grooming, a photo fix.

Recipe: Align both shots exactly (an edited version of the same shot is already aligned). Put 'after' above 'before' with a rectangular mask whose edge animates from left to right (or crop with an animated width + overlay), and add a thin white line and a handle at the edge. Move slowly with easing, pause in the middle, and come back.

Tags: before-after, wipe, mask, own-footage  
Reference: https://ffmpeg.org/ffmpeg-filters.html#overlay-1

### Word-by-word captions — Typography

Captions of 1–4 words at a time, synced to speech, with the current word or a key word highlighted by color or size.

When to use: In almost every talking video for Reels — most viewers watch without sound.

Recipe: Transcribe with word-level timestamps, split into short phrases (up to about 20 characters per line) and place them in the lower third, above the icon area. Use a bold font with a stroke or shadow for readability, highlight one key word in color, and add a short pop entrance (scale 90%→100% over 3 frames). For right-to-left languages, check text direction and the order of embedded English words.

Tags: captions, text, subtitles, talking-head  
Reference: https://ffmpeg.org/ffmpeg-filters.html#drawtext-1

### Typewriter text — Typography

Text appears letter by letter, sometimes with a blinking cursor.

When to use: For quotes, a simulated search, chat messages and investigative titles.

Recipe: Show a string that grows over time at 15–25 characters per second, with a '|' cursor blinking at 2 Hz after the last letter. For right-to-left languages, letters are added from right to left. Keep the full text on screen for at least 1.5 seconds before cutting.

Tags: text, typewriter, overlay  
Reference: Common editing technique

### VHS / camcorder look — Texture/Stylize

The look of an old videotape: soft resolution, color bleed, noise, scanlines, tracking bands and a date in the corner.

When to use: For nostalgia, flashbacks, 'back in the day' videos and home-video style clips.

Recipe: Downscale to about 360p and scale back up (to soften resolution), shift the chroma channels a few pixels (chromashift/rgbashift), reduce sharpness and add noise, scanlines and a vignette. Occasionally add a short horizontal tracking band, and a date or PLAY label in a monospace font. You can narrow to 4:3 with bars.

Tags: vhs, retro, noise, stylize  
Reference: https://ffmpeg.org/ffmpeg-filters.html#chromashift

### Datamosh / pixel bleed — Texture/Stylize

Pixels from the previous shot smear into the motion of the next — a deliberate compression artifact that looks like the image melting.

When to use: For aggressive transitions in music videos and gaming or electronic content; use briefly.

Recipe: The classic method: re-encode with distant keyframes and remove the I-frame at the start of the second shot, so B's motion vectors are applied to A's pixels. A more predictable alternative: animated noise/displacement combined with tblend. Limit it to 0.5–1.5 seconds and always end on a clean frame.

Tags: glitch, datamosh, transition, stylize  
Reference: Common editing technique

### Sketch / comic edge look — Texture/Stylize

Emphasizing outlines and reducing detail and colors so the video looks like a line drawing or comic.

When to use: For switching to an illustrated style, emphasizing a moment or a stylized intro.

Recipe: Clean noise (smartblur), extract lines with edgedetect=mode=colormix — or with edgedetect on a separate layer blended in multiply — and reduce colors (stepped curves / posterize). Halftone or paper texture completes a comic look. Keep it to a short segment.

Tags: sketch, comic, edge, stylize  
Reference: https://ffmpeg.org/ffmpeg-filters.html#edgedetect

### Kaleidoscope / mirror segments — Transform/Distort

The frame is mirrored into several symmetric segments that rotate — like a kaleidoscope.

When to use: For music videos, abstract visuals, nature and lights.

Recipe: Simple version: crop to a half or quarter, hflip/vflip and reassemble (hstack/vstack) for 2- or 4-way symmetry. For more segments, use geq or a shader that maps the polar angle to a segment. Animate a slow rotation of the source (not of the result) and keep it on the beat.

Tags: mirror, symmetry, distort, stylize  
Reference: https://ffmpeg.org/ffmpeg-filters.html#hflip

### Shatter / disintegrate — Transform/Distort

The object or frame breaks into shards or particles that fly outward, sometimes revealing the next shot.

When to use: For a punch on a strong beat, a logo exit or a character vanishing; use rarely.

Recipe: Separate the object with a mask (or take the whole frame), split it into shards (Voronoi or triangles) or particles, and give each shard an initial velocity from the impact point, rotation and gravity, with a fade-out. Add a short flash and shake at the moment of impact. Requires a compositing/3D engine (After Effects, Blender, or Canvas/WebGL in an HTML-to-video tool).

Tags: shatter, particles, impact, overlay  
Reference: Common editing technique
