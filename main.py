# Lesson 03 — Piano 🎹

**Difficulty:** ⭐⭐ Intermediate  
**Time:** 30 minutes  
**Grade:** 4–7  
**Concepts:** PWM, frequency, functions, dictionaries

---

## What you'll build

Turn your Airo Kit into a 4-key piano! Each button plays a musical note through the buzzer.

---

## What you'll learn

- What **PWM** (Pulse Width Modulation) is
- How sound frequency relates to musical pitch
- How to write reusable **functions**

---

## How the buzzer works

The buzzer makes sound by vibrating. We control how fast it vibrates using **PWM** —
rapidly switching the signal on and off at a specific **frequency**.

- 440 Hz = the note **A4** (concert pitch)
- Double the frequency = one octave higher
- The buzzer on GP5 is a *passive* buzzer — it needs PWM to make sound

---

## Code — Simple Piano

```python
from machine import Pin, PWM
import time

# Set up buttons (active LOW — pressed = 0)
buttons = [Pin(i, Pin.IN, Pin.PULL_UP) for i in range(6, 10)]

# Musical notes: C D E G (a pentatonic set — always sounds good!)
notes = [262, 294, 330, 392]   # C4, D4, E4, G4

buzzer = PWM(Pin(5))

def play_tone(frequency, duration=0.15):
    """Play a tone at the given frequency for the given duration."""
    buzzer.freq(frequency)
    buzzer.duty_u16(32768)   # 50% duty = loudest
    time.sleep(duration)
    buzzer.duty_u16(0)       # Silence
    time.sleep(0.02)         # Small gap between notes

# Play startup scale
for note in notes:
    play_tone(note, 0.1)

print("Piano ready! Press buttons A B C D")

while True:
    for i, btn in enumerate(buttons):
        if not btn.value():          # Button pressed (active LOW)
            play_tone(notes[i])
            print(f"Button {chr(65+i)} — {notes[i]} Hz")
```

---

## Full note dictionary

```python
NOTES = {
    "C4": 262, "D4": 294, "E4": 330, "F4": 349,
    "G4": 392, "A4": 440, "B4": 494,
    "C5": 523, "D5": 587, "E5": 659,
}

# Play a melody
melody = ["C4", "C4", "G4", "G4", "A4", "A4", "G4"]
durations = [0.3,  0.3,  0.3,  0.3,  0.3,  0.3,  0.6]

for note, dur in zip(melody, durations):
    play_tone(NOTES[note], dur)
```

---

## Try it yourself

1. Change the 4 notes to higher ones — what do you notice?
2. Record a melody by writing down which buttons you pressed, then replay it in code
3. Can you make Button D play a "wrong answer" buzzer sound?

---

## Key vocabulary

| Word | Meaning |
|---|---|
| **PWM** | Rapidly switching a pin on/off to control power or make sound |
| **Frequency** | How many times per second the buzzer vibrates — measured in Hz |
| **Pitch** | How high or low a sound is |
| **Function** | A named block of reusable code — `def my_function():` |

---

## Extension challenges

- 🌟 Play "Twinkle Twinkle Little Star" automatically
- 🌟🌟 Record button presses and play them back
- 🌟🌟🌟 Make a duet — use LEDs to show which note is playing while the buzzer sounds

---

*Previous: [Lesson 02](lesson-02-led-patterns.md) | Next: [Lesson 04 — Reaction Game](lesson-04-reaction-game.md)*
