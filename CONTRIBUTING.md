# PCB Fabrication Guide — Airo Science Kit v1

## Ordering from JLCPCB (Recommended for cost)

1. Go to https://jlcpcb.com
2. Click "Order Now" → upload the ZIP from `hardware/gerbers/airo-science-kit-v1-gerbers.zip`
3. Use these settings:

| Setting | Value |
|---|---|
| Base Material | FR4 |
| Layers | 2 |
| Dimensions | 150mm × 150mm |
| PCB Qty | 5 (prototype) or 100+ (production) |
| PCB Thickness | 1.6mm |
| PCB Color | Green (cheapest) or Blue |
| Silkscreen | White |
| Surface Finish | HASL (lead-free) |
| Outer Copper Weight | 1oz |
| Gold Fingers | No |
| Confirm Production File | No |
| Flying Probe Test | Fully Test |

**Estimated cost:**
- 5 boards: ~$2 each
- 100 boards: ~$1.20–$1.80 each

---

## Ordering from PCBWay (Alternative)

1. Go to https://pcbway.com
2. Click "PCB Instant Quote"
3. Same settings as above
4. PCBWay offers better customer support and slightly higher quality finish

---

## Ordering from Lion Circuits (India)

1. Go to https://www.lionbirdpcb.com
2. Upload Gerber ZIP
3. Select 2-layer, 150×150mm, HASL
4. Estimated cost: ₹500–900 for qty 5

---

## Gerber Files Included

| File | Description |
|---|---|
| F_Cu.gbr | Front copper layer |
| B_Cu.gbr | Back copper layer |
| F_Silkscreen.gbr | Front silkscreen |
| B_Silkscreen.gbr | Back silkscreen |
| F_Mask.gbr | Front soldermask |
| B_Mask.gbr | Back soldermask |
| Edge_Cuts.gbr | Board outline (150×150mm, 3mm radius corners) |
| PTH.drl | Plated through-hole drill file |
| NPTH.drl | Non-plated through-hole drill file |

---

## After Receiving Your Boards

1. Inspect for any obvious defects (scratches, missing silkscreen)
2. Solder components in this order:
   - Decoupling capacitors (C1, C2) first — smallest
   - Resistors (R1–R7)
   - Pin headers (H1, H2) for XIAO
   - LEDs — check polarity! Long leg (+) goes in square pad
   - Buzzer — check polarity marking on PCB
   - Buttons and slide switch
   - Battery holder last
3. Insert XIAO RP2040 into headers
4. Power on and test with `firmware/micropython/main.py`
