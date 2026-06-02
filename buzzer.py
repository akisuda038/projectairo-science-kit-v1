# Lesson 07 — Simon Says 🧠

**Difficulty:** ⭐⭐⭐ Advanced  
**Time:** 45 minutes  
**Grade:** 7–10  
**Concepts:** State machines, lists, game logic, functions, increasing difficulty

---

## What you'll build

The classic Simon Says memory game! A sequence of LEDs lights up — repeat it back using the buttons.
Each round adds one more step. How long can you remember?

---

## What you'll learn

- How to build a **state machine** (different modes: waiting → showing → player input → result)
- How to use **growing lists** to store a sequence
- How to structure a full **game loop**
- Thinking about **edge cases** (what if the player is too slow?)

---

## How the game works

```
START
  ↓
Generate new sequence (add 1 random step)
  ↓
SHOW sequence (flash LEDs with sounds)
  ↓
PLAYER INPUT (match the sequence with buttons)
  ↓
  ├── Correct → WIN ROUND → harder sequence → loop
  └── Wrong   → GAME OVER → show score → restart
```

---

## Code — Full Simon Says Game

```python
from machine import Pin, PWM
import time, random

leds    = [Pin(i, Pin.OUT) for i in range(4)]   # 4 LEDs for 4 buttons
buttons = [Pin(i, Pin.IN, Pin.PULL_UP) for i in range(6, 10)]
bz      = PWM(Pin(5))

# Notes for each button A B C D
TONES = [262, 330, 392, 523]   # C4, E4, G4, C5

def play(idx, dur=0.4):
    """Light LED and play tone for index idx."""
    leds[idx].on()
    bz.freq(TONES[idx]); bz.duty_u16(32768)
    time.sleep(dur)
    leds[idx].off()
    bz.duty_u16(0)
    time.sleep(0.05)

def flash_all(times=3):
    for _ in range(times):
        for l in leds: l.on()
        bz.freq(880); bz.duty_u16(32768)
        time.sleep(0.1)
        for l in leds: l.off()
        bz.duty_u16(0)
        time.sleep(0.1)

def game_over_sound():
    for f in [523, 440, 370, 294]:
        bz.freq(f); bz.duty_u16(32768)
        time.sleep(0.2)
    bz.duty_u16(0)

def wait_button(timeout_ms=4000):
    """Wait for a button press, return index or -1 on timeout."""
    start = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), start) < timeout_ms:
        for i, btn in enumerate(buttons):
            if not btn.value():
                # Debounce — wait for release
                while not btn.value():
                    time.sleep(0.01)
                return i
        time.sleep(0.01)
    return -1  # Timeout

# ── Main game loop ──────────────────────────────────────────
while True:
    sequence = []
    score    = 0

    print("\n=== SIMON SAYS ===")
    print("Watch the LEDs, then repeat the pattern!")
    print("Press any button to start...")

    # Wait for start
    wait_button(timeout_ms=60000)
    flash_all(2)
    time.sleep(0.5)

    # Game rounds
    game_active = True
    while game_active:
        # Add a new random step to the sequence
        sequence.append(random.randint(0, 3))
        level = len(sequence)
        print(f"\nRound {level} — sequence length: {level}")

        # Show the sequence (slower at first, speeds up)
        show_delay = max(0.2, 0.5 - level * 0.02)
        time.sleep(0.8)
        for idx in sequence:
            play(idx, dur=show_delay)
            time.sleep(0.05)

        # Player input phase
        print("Your turn!")
        for step, expected in enumerate(sequence):
            pressed = wait_button(timeout_ms=5000)

            if pressed == -1:
                print("Too slow!")
                game_active = False
                break

            play(pressed, dur=0.15)   # Feedback for player's press

            if pressed != expected:
                print(f"Wrong! Expected button {chr(65+expected)}, got {chr(65+pressed)}")
                game_active = False
                break

        if game_active:
            score = level
            print(f"✓ Correct! Score: {score}")
            # Victory beep
            bz.freq(1047); bz.duty_u16(32768)
            time.sleep(0.1); bz.duty_u16(0)
            time.sleep(0.6)

    # Game over
    print(f"\n=== GAME OVER ===")
    print(f"You reached level {score}!")
    if score >= 10:
        print("🏆 Amazing memory!")
    elif score >= 5:
        print("👏 Great job!")
    else:
        print("Keep practicing!")

    game_over_sound()
    flash_all(5)
    time.sleep(2)
```

---

## Try it yourself

1. Play a few rounds — what's the longest sequence you can remember?
2. Change `TONES` to use different notes — does it feel harder or easier?
3. Add a "lives" system — players get 3 mistakes before game over

---

## Key vocabulary

| Word | Meaning |
|---|---|
| **State machine** | A system that can be in one of several "states" — like waiting, showing, input |
| **Sequence** | An ordered list — the order matters! |
| **Debounce** | Waiting a moment after a button press to avoid counting one press twice |
| **Timeout** | A maximum time to wait — prevents the game from hanging forever |

---

## How a state machine works

```
[IDLE] ──start──→ [SHOWING] ──done──→ [INPUT] ──correct──→ [WIN_ROUND]
                                          │                      │
                                          └───wrong──→ [GAME_OVER]
                                                              │
                                                         [IDLE] ←──restart─┘
```

State machines are used everywhere in real software: traffic lights, vending machines,
video games, robot control systems, and web applications.

---

## Extension challenges

- 🌟 Add a high score that persists between games (store in a variable)
- 🌟🌟 Add a "speed mode" where the sequence shows faster each round
- 🌟🌟🌟 Two-player competitive mode — players alternate and the one who fails first loses

---

*Previous: [Lesson 06](lesson-06-thermometer.md)*

---

## What's next?

You've completed all 7 lessons! Here are ideas for your own projects:

- **Weather station** — combine light + temperature sensors, log data
- **Alarm system** — use light sensor to detect when a drawer is opened
- **Music box** — compose and play your own songs
- **Morse code decoder** — translate button taps to letters
- **Reaction tournament** — multiplayer version of Lesson 04

**Share your project!** Open a Pull Request on GitHub with your code and a short description.
Other Airo students around the world will be able to learn from what you build. 🚀
