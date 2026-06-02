# Lesson 02 — LED Patterns 🌈

**Difficulty:** ⭐ Beginner  
**Time:** 25 minutes  
**Grade:** 3–6  
**Concepts:** Lists, for loops, timing, binary numbers

---

## What you'll build

Control all 5 LEDs to create cool patterns — a running light, a bounce, and a binary counter.

---

## What you'll learn

- How to store multiple pins in a **list**
- How to use a **for loop** to step through items
- Introduction to **binary numbers** using LEDs

---

## Code — LED Chase

```python
from machine import Pin
import time

# Store all 5 LED pins in a list
leds = [Pin(i, Pin.OUT) for i in range(5)]

# Chase pattern — one LED at a time
while True:
    for led in leds:
        led.on()
        time.sleep(0.1)
        led.off()
```

---

## Code — Bounce (Knight Rider style)

```python
from machine import Pin
import time

leds = [Pin(i, Pin.OUT) for i in range(5)]

while True:
    # Go left to right
    for led in leds:
        led.on()
        time.sleep(0.08)
        led.off()
    # Go right to left
    for led in reversed(leds):
        led.on()
        time.sleep(0.08)
        led.off()
```

---

## Code — Binary Counter (0 to 31)

```python
from machine import Pin
import time

leds = [Pin(i, Pin.OUT) for i in range(5)]

while True:
    for number in range(32):          # 0 to 31
        for i in range(5):
            # Check each bit of the number
            leds[i].value((number >> i) & 1)
        print(f"Number: {number:2d}  Binary: {number:05b}")
        time.sleep(0.3)
```

---

## Try it yourself

1. Make all LEDs flash together 3 times, then chase once
2. Change the delay — how fast can you go before it looks like all LEDs are on?
3. Can you make only the even-numbered LEDs (0, 2, 4) light up?

---

## Key vocabulary

| Word | Meaning |
|---|---|
| **List** | A collection of items stored together — `[item1, item2, item3]` |
| **For loop** | Repeats once for each item in a list |
| **Binary** | A number system using only 0 and 1 |
| **Bit** | A single 0 or 1 — the smallest unit of digital information |

---

## Extension challenges

- 🌟 Make a "breathing" effect — fade using fast on/off switching
- 🌟🌟 Create your own custom pattern
- 🌟🌟🌟 Display the number of button presses in binary on the LEDs

---

*Previous: [Lesson 01](lesson-01-led-blink.md) | Next: [Lesson 03 — Piano](lesson-03-piano.md)*
