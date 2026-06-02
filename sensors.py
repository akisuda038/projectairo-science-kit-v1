# Lesson 01 — LED Blink 💡

**Difficulty:** ⭐ Beginner  
**Time:** 20 minutes  
**Grade:** 3–5  
**Concepts:** Digital output, loops, delays

---

## What you'll build

Make a single LED blink on and off like a heartbeat. This is the "Hello World" of electronics!

---

## What you'll learn

- What a digital output is (ON = 1, OFF = 0)
- How to use a loop to repeat actions forever
- How to control time with `time.sleep()`

---

## Parts used

- 1 LED (any color — try Red on GP0)
- Already wired on your Airo Science Kit PCB ✅

---

## Circuit reminder

```
XIAO GP0 → 330Ω resistor → LED (+) → LED (-) → GND
```

The resistor limits current so the LED doesn't burn out. It's already on your PCB!

---

## Code — MicroPython

Open Thonny, paste this code, and click **Run**:

```python
from machine import Pin
import time

# Create a Pin object for GP0 (Red LED), set as OUTPUT
led = Pin(0, Pin.OUT)

# Loop forever
while True:
    led.on()          # Turn LED ON
    time.sleep(0.5)   # Wait 0.5 seconds
    led.off()         # Turn LED OFF
    time.sleep(0.5)   # Wait 0.5 seconds
```

---

## Try it yourself

1. Change `0.5` to `0.1` — what happens?
2. Change `0.5` to `2.0` — what happens?
3. Can you make the LED blink in a pattern like SOS? (3 short, 3 long, 3 short)

---

## MakeCode (Blocks)

1. Go to makecode.com
2. Add a **forever** loop
3. Inside: **digital write pin P0 = 1**, **pause 500ms**, **digital write pin P0 = 0**, **pause 500ms**
4. Download and flash the `.uf2` file

---

## Key vocabulary

| Word | Meaning |
|---|---|
| **Digital** | Only two values: ON (1) or OFF (0) |
| **Output** | The microcontroller is *sending* a signal |
| **Loop** | Code that repeats over and over |
| **Delay** | A pause — the microcontroller waits before continuing |

---

## Extension challenges

- 🌟 Blink all 5 LEDs at the same time
- 🌟🌟 Blink them one at a time in sequence (LED chase!)
- 🌟🌟🌟 Morse code your name using long and short blinks

---

*Next lesson: [Lesson 02 — LED Patterns](lesson-02-led-patterns.md)*
