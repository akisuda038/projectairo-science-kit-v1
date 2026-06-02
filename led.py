# Lesson 05 — Light Meter 🌤️

**Difficulty:** ⭐⭐ Intermediate  
**Time:** 30 minutes  
**Grade:** 5–8  
**Concepts:** Analog input, ADC, voltage dividers, mapping values

---

## What you'll build

A light meter that reads the LDR sensor and shows brightness as a bar graph on the 5 LEDs.
Cover the sensor with your hand — the LEDs go out. Shine a torch — they all light up!

---

## What you'll learn

- The difference between **analog** and **digital** signals
- How an **ADC** (Analog-to-Digital Converter) works
- How a **voltage divider** circuit works
- How to **map** a sensor range to an output range

---

## How the LDR circuit works

```
3V3 ──┬── LDR (resistance drops in light) ──┬── GP26 (ADC)
      │                                      │
      │                                     10K (fixed)
      │                                      │
     GND ─────────────────────────────────  GND
```

- In **bright light**: LDR resistance drops → more voltage at GP26 → high ADC reading
- In **darkness**: LDR resistance rises → less voltage at GP26 → low ADC reading
- ADC on RP2040 is **12-bit** (values 0–4095), but MicroPython gives us 16-bit (0–65535)

---

## Code — Light Bar Graph

```python
from machine import ADC, Pin
import time

ldr     = ADC(Pin(26))    # LDR on GP26
leds    = [Pin(i, Pin.OUT) for i in range(5)]

def read_light_percent():
    """Read LDR and return light level 0–100%."""
    raw = ldr.read_u16()         # 0–65535
    return raw / 65535 * 100

def set_bar(percent):
    """Light up LEDs like a bar graph based on percentage."""
    count = round(percent / 100 * 5)
    for i, led in enumerate(leds):
        led.value(1 if i < count else 0)

print("Light Meter running — cover sensor to dim, shine light to brighten")

while True:
    level = read_light_percent()
    set_bar(level)
    print(f"Light: {level:.1f}%  {'█' * int(level/20)}")
    time.sleep(0.1)
```

---

## Code — Night Light

```python
from machine import ADC, Pin, PWM
import time

ldr    = ADC(Pin(26))
leds   = [Pin(i, Pin.OUT) for i in range(5)]
buzzer = PWM(Pin(5))

while True:
    raw   = ldr.read_u16()
    level = raw / 65535 * 100

    if level < 20:     # Dark!
        for led in leds: led.on()
        buzzer.freq(440); buzzer.duty_u16(8000)
    else:
        for led in leds: led.off()
        buzzer.duty_u16(0)

    time.sleep(0.2)
```

---

## Try it yourself

1. Print the raw ADC value — what is it in a dark room? Bright sunlight?
2. Make just one LED act as a "night light" — on when dark, off when bright
3. Can you calibrate the sensor? (Set min/max based on your environment)

---

## Key vocabulary

| Word | Meaning |
|---|---|
| **Analog** | A continuous signal — any value between min and max |
| **Digital** | Only two values: 0 or 1 |
| **ADC** | Analog-to-Digital Converter — turns voltage into a number |
| **Voltage divider** | Two resistors that split a voltage — used to read variable sensors |
| **LDR** | Light Dependent Resistor — resistance changes with light level |

---

## Science connection

LDRs are used in:
- Automatic street lights (turn on at dusk)
- Camera exposure meters
- Solar-powered garden lights
- Burglar alarm beams

---

## Extension challenges

- 🌟 Log light readings every 10 seconds — does your classroom change throughout the day?
- 🌟🌟 Build a sunrise alarm — gradually light up LEDs as a simulated sunrise
- 🌟🌟🌟 Combine with temperature (Lesson 06) to build a weather station dashboard

---

*Previous: [Lesson 04](lesson-04-reaction-game.md) | Next: [Lesson 06 — Thermometer](lesson-06-thermometer.md)*
