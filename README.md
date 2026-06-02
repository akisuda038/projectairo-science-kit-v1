# 🔬 Airo Science Kit — Version 1

> An open-source, student-buildable electronics kit designed for Project Airo's STEM programs. Powered by the Seeed XIAO RP2040. Built for Grades 3–10.

[![License: CERN OHL v2](https://img.shields.io/badge/Hardware-CERN%20OHL%20v2-blue)](https://ohwr.org/cern_ohl_s_v2.txt)
[![License: MIT](https://img.shields.io/badge/Firmware-MIT-green)](LICENSE-FIRMWARE)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/Curriculum-CC%20BY--SA%204.0-orange)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Project Airo](https://img.shields.io/badge/Project-Airo-purple)](https://projectairo.com)

---

## What is this?

The Airo Science Kit v1 is a **custom PCB-based electronics learning kit** designed so students can:

- Learn real electronics concepts hands-on
- Program with **drag-and-drop blocks** (MakeCode) or **MicroPython**
- Build games, instruments, sensors, and more — no breadboard wiring required
- **Contribute their own lessons** back to this repository

The kit costs approximately **$7.80 per unit** at scale — a fraction of commercial alternatives like LEGO SPIKE Prime (~$330).

---

## Kit Contents

| Component | Qty | Purpose |
|---|---|---|
| Seeed XIAO RP2040 | 1 | Microcontroller brain |
| 5mm LEDs (R/G/Y/B/W) | 5 | Visual output, GP0–GP4 |
| 330Ω resistors | 5 | LED current limiting |
| Passive buzzer 3V | 1 | Audio output, GP5 (PWM) |
| Tactile push buttons | 4 | User input A/B/C/D, GP6–GP9 |
| Slide switch | 1 | Power on/off |
| LDR (light sensor) | 1 | Analog input, GP26 |
| NTC thermistor 10K | 1 | Temperature sensing, GP27 |
| 10K resistors | 2 | Voltage dividers for sensors |
| AA 2× battery holder | 1 | Standalone 3V power |
| Decoupling capacitors 100nF | 2 | Power rail stability |
| Custom PCB | 1 | 150mm × 150mm, 2-layer FR4 |

**Estimated cost per kit: ~$7.80** (qty 100+, JLCPCB fabrication)

---

## PCB Layout

The board is divided into four clearly silkscreened zones:

```
┌─────────────────────────────────────┐
│  Zone A — Brain                     │
│  XIAO RP2040 on stamp headers       │
│  USB-C facing board edge            │
├──────────────────┬──────────────────┤
│  Zone B — Output │  Zone D — Sense  │
│  5 LEDs in row   │  LDR + Thermist. │
│  Buzzer          │  Voltage dividers│
├──────────────────┴──────────────────┤
│  Zone C — Input                     │
│  Buttons: [A]  [B]  [C]  [D]        │
└─────────────────────────────────────┘
```

- Rounded PCB corners for safety
- Large silkscreen labels on every component
- HASL or ENIG finish
- XIAO removable — reusable across kits

---

## Repository Structure

```
science-kit-v1/
├── hardware/
│   ├── schematic/          # KiCad schematic files (.kicad_sch)
│   ├── pcb/                # KiCad PCB layout (.kicad_pcb)
│   ├── gerbers/            # Fabrication-ready Gerber files
│   └── bom.csv             # Full bill of materials with part numbers
│
├── firmware/
│   ├── micropython/        # MicroPython starter scripts
│   │   ├── main.py         # Entry point
│   │   ├── led.py          # LED helpers
│   │   ├── buzzer.py       # PWM tone helpers
│   │   └── sensors.py      # LDR + thermistor helpers
│   └── makecode/           # MakeCode .uf2 files for block coding
│
├── curriculum/
│   ├── lesson-01-led-blink.md
│   ├── lesson-02-led-patterns.md
│   ├── lesson-03-piano.md
│   ├── lesson-04-reaction-game.md
│   ├── lesson-05-light-meter.md
│   ├── lesson-06-thermometer.md
│   └── lesson-07-simon-says.md
│
├── assets/
│   ├── pcb-photo.jpg
│   ├── pinout-diagram.png
│   └── zone-diagram.png
│
├── LICENSE-HARDWARE        # CERN OHL v2
├── LICENSE-FIRMWARE        # MIT
├── LICENSE-CURRICULUM      # CC BY-SA 4.0
└── README.md
```

---

## Getting Started

### 1. Set up your XIAO RP2040

**Option A — MakeCode (Blocks, no install needed):**
1. Visit [makecode.com](https://makecode.com) in any browser
2. Download the `.uf2` file from `firmware/makecode/`
3. Hold the BOOT button on the XIAO while plugging in USB-C
4. A USB drive called `RPI-RP2` appears — drag the `.uf2` file onto it
5. The board reboots and your program runs

**Option B — MicroPython (Thonny IDE):**
1. Download [Thonny](https://thonny.org) — free, runs on Windows/Mac/Linux/Chromebook
2. Flash MicroPython firmware: go to **Tools → Options → Interpreter → Install or update MicroPython**
3. Select `RP2040` and install
4. Open any file from `firmware/micropython/` and click Run

---

### 2. Pin Reference

| GPIO | Connected to | Type |
|---|---|---|
| GP0 | LED Red | Digital OUT |
| GP1 | LED Green | Digital OUT |
| GP2 | LED Yellow | Digital OUT |
| GP3 | LED Blue | Digital OUT |
| GP4 | LED White | Digital OUT |
| GP5 | Buzzer | PWM OUT |
| GP6 | Button A | Digital IN (pull-up) |
| GP7 | Button B | Digital IN (pull-up) |
| GP8 | Button C | Digital IN (pull-up) |
| GP9 | Button D | Digital IN (pull-up) |
| GP26 | LDR | Analog IN (ADC0) |
| GP27 | Thermistor | Analog IN (ADC1) |

---

### 3. Your first program (MicroPython)

```python
from machine import Pin
import time

# Set up LEDs
leds = [Pin(i, Pin.OUT) for i in range(5)]

# Chase pattern
while True:
    for led in leds:
        led.on()
        time.sleep(0.1)
        led.off()
```

---

## Starter Activities

| Activity | Difficulty | Concepts |
|---|---|---|
| LED Blink | ⭐ Beginner | Digital output, loops |
| LED Patterns | ⭐ Beginner | Lists, timing |
| Piano | ⭐⭐ Intermediate | PWM, frequency, functions |
| Reaction Game | ⭐⭐ Intermediate | Random, input, timing |
| Light Meter | ⭐⭐ Intermediate | ADC, analog reading, mapping |
| Thermometer | ⭐⭐ Intermediate | Math, sensors, conditions |
| Simon Says | ⭐⭐⭐ Advanced | State machines, arrays, game logic |

Full lesson guides with step-by-step instructions are in the [`curriculum/`](curriculum/) folder.

---

## How to Contribute

This kit is built by and for students. Here's how to add your own lesson:

1. **Fork** this repository
2. Create a new file in `curriculum/` — use an existing lesson as a template
3. Add your MicroPython code in `firmware/micropython/`
4. Open a **Pull Request** with a short description of what your activity teaches
5. A Project Airo mentor will review and merge it

### Contribution ideas
- New games using the buttons and LEDs
- Musical compositions for the buzzer
- Science experiments using the sensors
- MakeCode block versions of existing Python lessons
- Translations of lessons into other languages

---

## Fabricating Your Own PCB

All hardware files are open source under the CERN OHL v2 license. Any school or maker can order their own boards:

1. Download the Gerber files from `hardware/gerbers/`
2. Upload to [JLCPCB](https://jlcpcb.com) or [PCBWay](https://pcbway.com)
3. Select: 2-layer FR4 · 150×150mm · HASL finish · qty 5 minimum
4. Estimated cost: ~$2 per board at qty 100

---

## About Project Airo

Project Airo is a 501(c)(3) nonprofit based in San Ramon, California, dedicated to empowering students in Grades 3–10 through STEM, mentorship, and hands-on learning.

- 🌐 [projectairo.com](https://projectairo.com)
- 📧 info@airo.org
- 🏆 Congressional App Challenge mentor organization

Programs include: Robotics camps, ML/AI Bootcamp, VEX RoboReach, Programming Basics Camp, and Connect College.

---

## Licenses

| Content | License |
|---|---|
| Hardware (PCB, schematic) | [CERN Open Hardware Licence v2](LICENSE-HARDWARE) |
| Firmware (MicroPython code) | [MIT License](LICENSE-FIRMWARE) |
| Curriculum (lessons, guides) | [CC BY-SA 4.0](LICENSE-CURRICULUM) |

---

*Built with ❤️ by Project Airo students and mentors.*
