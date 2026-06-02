# Contributing to Airo Science Kit v1

First off — thank you for contributing! This kit is built by students, for students.
Every lesson, game, and experiment you add helps kids around the world learn electronics and coding.

---

## Ways to contribute

| Type | What it is | Skill needed |
|---|---|---|
| New lesson | A step-by-step activity using the kit | Writing + any coding |
| MicroPython code | A new program or helper module | Python |
| MakeCode blocks | A visual block version of a lesson | MakeCode |
| Bug fix | Fix a mistake in existing code or docs | Varies |
| Translation | Translate a lesson into another language | Language skills |
| PCB improvement | Suggest or submit a hardware change | KiCad / electronics |

---

## How to submit a new lesson

### Step 1 — Fork the repository

Click **Fork** at the top right of the GitHub page.
This creates your own copy of the repository.

### Step 2 — Create your lesson file

Create a new Markdown file in `curriculum/`:

```
curriculum/lesson-08-your-activity-name.md
```

Copy the template below to get started.

### Step 3 — Add your code

Add your MicroPython file to `firmware/micropython/`:

```
firmware/micropython/your-activity-name.py
```

### Step 4 — Open a Pull Request

- Click **Pull Request** → **New Pull Request**
- Give it a clear title: `Add Lesson 08: Morse Code Decoder`
- Write a short description of what students will learn
- A Project Airo mentor will review and merge it!

---

## Lesson template

Copy this into your new `curriculum/lesson-XX-name.md` file:

```markdown
# Lesson XX — Title Here 🎯

**Difficulty:** ⭐ Beginner / ⭐⭐ Intermediate / ⭐⭐⭐ Advanced
**Time:** XX minutes
**Grade:** X–X
**Concepts:** concept1, concept2, concept3

---

## What you'll build

One sentence describing what the student makes.

---

## What you'll learn

- Bullet point learning goals

---

## Code

```python
# Your MicroPython code here
```

---

## Try it yourself

1. Modification idea 1
2. Modification idea 2
3. Modification idea 3

---

## Key vocabulary

| Word | Meaning |
|---|---|
| **Term** | Definition |

---

## Extension challenges

- 🌟 Easy challenge
- 🌟🌟 Medium challenge
- 🌟🌟🌟 Hard challenge
```

---

## Code style guide

- Use clear variable names: `light_level` not `ll`
- Add a comment to every non-obvious line
- Include a docstring for every function
- Test your code on a real XIAO RP2040 before submitting
- Keep imports at the top of the file
- Use `time.sleep()` not `utime.sleep()` (MicroPython alias works fine)

---

## Hardware contribution guide

If you'd like to suggest a PCB change:

1. Open a GitHub **Issue** describing the change and why
2. If you have KiCad skills, fork the repo and modify `hardware/schematic/` and `hardware/pcb/`
3. Run DRC (Design Rule Check) in KiCad before submitting
4. Include a screenshot of your change in the Pull Request

---

## Code of conduct

- Be kind and encouraging — contributors of all ages and skill levels are welcome
- Give constructive feedback in reviews
- Credit others when you build on their work
- Remember: every expert was once a beginner

---

## Questions?

- Open a GitHub **Issue** with the `question` label
- Email us at **info@airo.org**
- Visit **[projectairo.com](https://projectairo.com)**

---

*Built with ❤️ by Project Airo students and mentors.*
