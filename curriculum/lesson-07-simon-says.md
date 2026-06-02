# Assets — Airo Science Kit v1

This folder contains images and diagrams used in the README and curriculum lessons.

## Files

| File | Description | Status |
|---|---|---|
| `pcb-photo.jpg` | Photo of the assembled PCB | Add after fabrication |
| `pinout-diagram.png` | Full pinout diagram showing all GPIO connections | Add after PCB design |
| `zone-diagram.png` | Color-coded zone diagram (A/B/C/D) | Add after PCB design |
| `schematic-preview.png` | KiCad schematic screenshot | Add after KiCad design |
| `airo-logo.png` | Project Airo logo for silkscreen | Available at projectairo.com |

## How to generate pinout diagram

1. Complete the KiCad PCB layout
2. Export a 3D render: KiCad PCB Editor → File → Export → 3D Model
3. Screenshot from top view with zone labels overlaid
4. Or use KiCanvas (https://kicanvas.org) to generate a shareable web view

## Image guidelines

- Minimum resolution: 1200px wide for GitHub README display
- Format: PNG for diagrams, JPG for photos
- Zone diagram: use colors matching the spec
  - Zone A (Brain): Blue `#3B82F6`
  - Zone B (Output): Green `#22C55E`
  - Zone C (Input): Amber `#F59E0B`
  - Zone D (Sense): Gray `#6B7280`
