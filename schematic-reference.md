# PCB Design Notes — Airo Science Kit v1

## Software

Design tool: KiCad 8 (free download: https://www.kicad.org)

Files:
- `hardware/schematic/airo-science-kit-v1.kicad_sch` — schematic
- `hardware/pcb/airo-science-kit-v1.kicad_pcb` — PCB layout
- `hardware/gerbers/` — fabrication-ready Gerber files

---

## Board Specifications

| Parameter | Value |
|---|---|
| Board size | 150mm × 150mm |
| Layers | 2 (Front Cu + Back Cu) |
| Material | FR4 |
| Thickness | 1.6mm |
| Surface finish | HASL (lead-free) or ENIG |
| Copper weight | 1oz (35µm) |
| Min trace width | 0.3mm signal / 0.5mm power |
| Min clearance | 0.2mm |
| Corner radius | 3mm (rounded for safety) |
| Soldermask | Green (or blue) both sides |
| Silkscreen | White both sides |

---

## Layer Stack

| Layer | Use |
|---|---|
| F.Cu | Signal traces, component pads |
| B.Cu | GND copper pour |
| F.Silkscreen | Component labels, zone names, logos |
| B.Silkscreen | Assembly notes, website URL |
| F.Mask | Expose pads on front |
| B.Mask | Expose pads on back |
| Edge.Cuts | Board outline with rounded corners |

---

## Key Design Decisions

### XIAO on female pin headers
The XIAO RP2040 sits on 2× 7-pin female headers (2.54mm pitch).
This makes it:
- Easy for students to install — just press down
- Removable — one XIAO can be used across multiple kits
- Replaceable — if a XIAO is damaged, only the $5 module is lost

### Through-hole components only
All components are through-hole (THT) — no surface-mount (SMD).
Reasons:
- Students can solder THT components in a workshop
- Easier to inspect and debug
- Larger pads = more forgiving

### Zone silkscreen labels
Each zone (A/B/C/D) has a large silkscreen label visible from 30cm away.
Component designators (R1, LED2, etc.) are printed next to every component.
LED polarity is marked with a + symbol at the anode pad.

### USB-C accessibility
The XIAO's USB-C port faces the board edge so students can plug in easily
without removing the module from the headers.

### Battery holder placement
The AA 2× battery holder is on the underside of the board near Zone C.
A JST-PH 2.0 connector can be used instead for cleaner assembly.

---

## Footprints Used

| Component | KiCad Footprint |
|---|---|
| XIAO RP2040 | Custom stamp header footprint (see hardware/schematic/) |
| 5mm LED | LED_THT:LED_D5.0mm |
| 330Ω / 10K resistors | Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm |
| Buzzer | Buzzer_Beeper:Buzzer_TDK_PS1240P02BT_D12.0mm_P7.6mm |
| Tactile button | Button_Switch_THT:SW_PUSH_6mm |
| Slide switch | Button_Switch_THT:SW_Slide_1P2T_CK_OS102011MA1QN1 |
| LDR | Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm |
| NTC thermistor | Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm |
| 100nF capacitor | Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm |
| AA battery holder | Battery:BatteryHolder_Keystone_2462_2xAA |
| Pin headers | Connector_PinHeader_2.54mm:PinHeader_1x07_P2.54mm_Vertical |

---

## Ordering Checklist (before sending Gerbers)

- [ ] Run DRC (Design Rules Check) — zero errors
- [ ] Check all component courtyard overlaps
- [ ] Verify USB-C is at board edge
- [ ] Confirm LED polarity silkscreen is correct (+ at anode)
- [ ] Check 3mm corner radius on Edge.Cuts
- [ ] Verify GND copper pour connects properly on B.Cu
- [ ] Export Gerbers: F.Cu, B.Cu, F.Silkscreen, B.Silkscreen, F.Mask, B.Mask, Edge.Cuts
- [ ] Export drill files: PTH.drl, NPTH.drl
- [ ] Zip all Gerber files
- [ ] Upload to JLCPCB and verify preview

---

## Version History

| Version | Date | Notes |
|---|---|---|
| v1.0 | 2024 | Initial release — XIAO RP2040, 5 LEDs, 4 buttons, LDR, NTC |
