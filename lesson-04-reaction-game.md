# Lesson 06 — Thermometer 🌡️

**Difficulty:** ⭐⭐ Intermediate  
**Time:** 30 minutes  
**Grade:** 6–9  
**Concepts:** NTC thermistors, Steinhart-Hart equation, math in code, conditions

---

## What you'll build

A real thermometer that reads room temperature and shows it on the LEDs.
Pinch the sensor with your fingers — watch the temperature climb!

---

## What you'll learn

- How an **NTC thermistor** works
- How to use **math** to convert a voltage reading into temperature
- How to use **if/elif/else** conditions to trigger actions

---

## How the thermistor works

An NTC (Negative Temperature Coefficient) thermistor **decreases in resistance** as temperature rises.

```
3V3 ──── NTC thermistor ──┬── GP27 (ADC)
                          │
                         10K (fixed resistor)
                          │
                         GND
```

We read the voltage at the midpoint, then use the **Beta equation** to calculate temperature:

```
1/T = 1/T₀ + (1/β) × ln(R/R₀)
```

Don't worry — the code does all the math!

---

## Code — Thermometer

```python
from machine import ADC, Pin, PWM
import math, time

adc    = ADC(Pin(27))      # Thermistor on GP27
leds   = [Pin(i, Pin.OUT) for i in range(5)]
buzzer = PWM(Pin(5))

# NTC 10K @ 25°C, Beta = 3950
R_FIXED   = 10000
R_NOM     = 10000
T_NOM     = 25       # °C
BETA      = 3950

def read_temp_c():
    raw = adc.read_u16()
    if raw == 0: return 0
    r = R_FIXED * (65535 / raw - 1)          # Thermistor resistance
    t = 1.0 / (math.log(r / R_NOM) / BETA + 1.0 / (T_NOM + 273.15))
    return round(t - 273.15, 1)              # Kelvin → Celsius

def temp_to_leds(temp_c):
    """
    LED bar based on temperature range 15°C–35°C:
    15°C = 0 LEDs, 35°C = 5 LEDs
    """
    mapped = (temp_c - 15) / (35 - 15) * 5
    count  = max(0, min(5, round(mapped)))
    for i, led in enumerate(leds):
        led.value(1 if i < count else 0)

def beep(f=880, d=0.05):
    buzzer.freq(f); buzzer.duty_u16(32768)
    time.sleep(d);  buzzer.duty_u16(0)

print("Thermometer ready — pinch the sensor to raise temp!")

while True:
    temp = read_temp_c()
    temp_to_leds(temp)
    print(f"Temperature: {temp}°C  ({temp * 9/5 + 32:.1f}°F)")

    if temp > 30:
        print("  ⚠️  Too warm!")
        beep(1047, 0.1)
    elif temp < 18:
        print("  🧊 Cold!")
        beep(262, 0.2)

    time.sleep(0.5)
```

---

## Try it yourself

1. What temperature is the room right now?
2. Pinch the thermistor with your fingers — how high can you get it?
3. Blow cool air on the thermistor — how fast does it drop?

---

## Key vocabulary

| Word | Meaning |
|---|---|
| **NTC** | Negative Temperature Coefficient — resistance goes down as heat goes up |
| **Thermistor** | A resistor that changes value with temperature |
| **Kelvin** | A temperature scale starting at absolute zero (0K = -273.15°C) |
| **Beta (β)** | A constant that describes how quickly a thermistor's resistance changes |

---

## Science connection

Thermistors are used in:
- Medical thermometers
- Car engine temperature sensors
- Refrigerators and air conditioners
- Weather stations
- 3D printer heated beds

---

## Extension challenges

- 🌟 Add Fahrenheit display — convert using `F = C × 9/5 + 32`
- 🌟🌟 Log temperature every minute and find the daily max/min
- 🌟🌟🌟 Combine with LDR (Lesson 05) — build a full environment monitor

---

*Previous: [Lesson 05](lesson-05-light-meter.md) | Next: [Lesson 07 — Simon Says](lesson-07-simon-says.md)*
