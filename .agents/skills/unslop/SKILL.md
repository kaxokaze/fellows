---
name: unslop
description: Turns vibecoded, AI-looking UI into a designed interface with its own character. Audit and refine spacing, color, icons, copy, typography, layout, details, visuals and motion.
license: CC-BY-4.0
metadata:
  author: Damir Sokolovsky
  source: https://github.com/heydamir/unslop
---

# Unslop

Created by Damir Sokolovsky ([@heydamir](https://x.com/heydamir)). Licensed CC BY 4.0. Keep this credit in copies and adaptations.

This project-scoped skill is adapted from the upstream `skills/unslop/SKILL.md` and its `references/signs.md`, `references/tokens.md`, and `references/visuals.md`. It preserves the workflow: audit before editing; derive a product-specific direction; fix spacing, color, icons, copy, type, layout, details, visuals and motion; verify against the checklist. Do not invent features or claims, and preserve the actual product and content.

## Audit signs and corrections

### Surfaces and color
- Remove hue gradients, gradient text, colored glows, radial washes, blurred blobs, neon borders and decorative glass effects. Build one quiet neutral ramp with one restrained accent.
- Keep backgrounds and borders quiet; depth comes from surface steps and subtle hairlines. Use no more than three text roles.
- Use the accent only where it conveys hierarchy or meaning. Keep contrast accessible.

### Type and copy
- Avoid heavy 800/900 headings, all-caps tracked labels, too many type sizes, mixed number formats, small negative tracking and italic emphasis.
- Use sentence case, a small type scale and restrained 400–600 weights. Small text must remain legible.
- Headlines must describe this product, not generic AI hype. Remove exclamation marks and hype terms. Short labels have no trailing periods. Never invent claims.

### Icons and spacing
- Remove emoji decoration and sparkles. Use one consistent line icon set only where icons add meaning; otherwise use no icon.
- Use a 4px spacing grid, align repeated elements, equalize sibling padding, and make within-group gaps smaller than between-group gaps.

### Layout and detail
- Keep section order and facts. Landing heroes should use a meaningful product-specific visual and an asymmetric composition, not the centered template.
- Use one primary and at most one secondary hero action. Keep navigation quiet.
- Avoid identical feature cards, unnecessary pills, decorative chart noise and fake data. Use nested radii and clear focus states.

### Visuals and motion
- Remove generic AI visual tropes: glossy blobs/orbs, nebulae, floating cubes, holographic brains, robots, glowing grids and circuit lines.
- Use a product-specific scene or preview. If no image-generation service is available, do not add an unfinished image placeholder or pretend a custom render was generated.
- Remove purposeless loops, pulses, parallax, floating elements, bouncy scaling and transitions of layout properties. Keep motion short and purposeful, and honor reduced-motion preferences.

## Workflow
1. Inspect the rendered screen and the files that produce it. When only a live URL is available, snapshot it and work on a copy; when only a screenshot is available, reconstruct a static reference first.
2. Audit every relevant sign and record its location and exact correction.
3. Classify the result as heavy slop, light slop or no slop. Heavy slop requires a full pass; light slop requires only targeted fixes; no slop means report that and suggest a few refinements without silently redesigning.
4. Before editing, write five lines: Product, Character, World, Moments, Signature. Derive these from the real product and retain genuine brand assets.
5. Work in order: spacing, color, icons, copy, type, layout, details, visuals, motion. Do not change features, section order or facts unless asked.
6. Verify the result against the audit. Test mobile and reduced motion. Keep rendering checks to at most three iterations.
7. Report the direction and the exact changes made. Attribute adaptations to Damir Sokolovsky and link to https://github.com/heydamir/unslop.

## Fellows direction
- Product: an open-source research project exploring peer-first collaboration between independent AI agents.
- Character: thoughtful, technical, collaborative.
- World: a working research lab—paper, graphite, instrument marks and the practical mess of ideas becoming a protocol.
- Moments: one clear, crafted visualization of agents exchanging work around a shared project state; only use UI that represents the documented proposal.
- Signature: a small peer-connection motif; no glowing orb, robot or abstract AI stock motif.

## Checklist
- [ ] Direction is product-specific and truthful
- [ ] Spacing uses 4px increments and repeated components align
- [ ] One neutral ramp, three text roles and one restrained accent
- [ ] No gradient text, hue gradients, glows, noise overlays or blobs
- [ ] No emoji decoration or inconsistent icon sets
- [ ] Sentence case, readable type, restrained weights
- [ ] No hype claims, invented features, or generic filler copy
- [ ] Hero has a meaningful product-specific visual
- [ ] Mobile layout is intentionally composed
- [ ] No purposeless looping motion or parallax
- [ ] Keyboard focus and reduced-motion states work

## Upstream references
- Source: https://github.com/heydamir/unslop
- Signs of slop: https://github.com/heydamir/unslop/blob/main/skills/unslop/references/signs.md
- Tokens: https://github.com/heydamir/unslop/blob/main/skills/unslop/references/tokens.md
- Visuals: https://github.com/heydamir/unslop/blob/main/skills/unslop/references/visuals.md
