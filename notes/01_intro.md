# Section 1: Introduction + CS Fundamentals

**Course:** Python for AI Engineering (Towards AI Academy)
**Instructor:** Louis-François Bouchard
**Status:** Complete

---

## What Programming Is

Programming is giving a computer precise, step-by-step instructions in a language it understands. The computer does exactly what you tell it to. Nothing more, nothing less. That literalness is the whole challenge.

The core cycle at every skill level is:

**Plan → Code → Test → Refine**

You identify the problem, write a solution, check for bugs, and improve. Then repeat. This loop doesn't go away as you get better. It just gets faster.

---

## Why Python

Python reads almost like English, which makes it beginner-friendly. It also dominates the AI and data science community, so the libraries, tutorials, and job relevance are all there. It's an interpreted language, meaning the interpreter runs your code line by line. Compiled languages like C++ translate the whole program first before running it.

---

## CS Fundamentals

### Syntax
The formal rules of a programming language. Think of it like grammar. Break the rules and the computer doesn't understand you. Every language has its own syntax.

### Variables and Data Types
Variables are named containers for storing data. The main data types in Python are:
- `int`: whole numbers (e.g., `42`)
- `float`: decimals (e.g., `3.14`)
- `str`: text (e.g., `"hello"`)
- `bool`: true or false

### Data Structures
Ways to organize and store collections of data:
- **List**: ordered, mutable collection: `[1, 2, 3]`
- **Dictionary**: key-value pairs: `{"name": "Garret", "age": 25}`
- **Tuple**: ordered, immutable: `(1, 2, 3)`
- **Set**: unordered, unique values: `{2, 1, 3}`

### Input and Output
Programs interact with users through `input()` (reads from the user) and `print()` (displays output). These are the simplest form of a program talking to the outside world.

### Control Structures
Control flow determines what runs and when:
- **Conditionals** (`if/elif/else`): make decisions based on conditions
- **Loops**: `while` runs while a condition is true; `for` iterates over a sequence or collection

### Functions
Reusable blocks of code that take inputs (parameters) and return outputs. The DRY principle applies here: Don't Repeat Yourself. If you're writing the same logic twice, put it in a function.

### Classes and Objects
Classes are blueprints. Objects are instances of those blueprints. A `Dog` class might have attributes like `name` and `breed`, and methods like `bark()`. This is the foundation of object-oriented programming (OOP).

### Algorithms and Principles
An algorithm is a finite, well-defined sequence of steps for solving a problem or performing a computation. Two principles worth remembering early:
- **DRY** (Don't Repeat Yourself): avoid duplicating logic
- **KISS** (Keep It Simple, Stupid): simple code is easier to read, debug, and maintain

### APIs
An API (Application Programming Interface) is a set of rules that lets one program request data or services from another. Example: asking a weather server for today's forecast via an HTTP request. You'll use these heavily when integrating LLMs into projects.

---

## Tools and Workflow

| Tool | Purpose |
|---|---|
| VS Code | Primary IDE for writing and running Python |
| Terminal | Running scripts, installing packages |
| pip | Package manager for installing libraries |
| Virtual environments | Isolating project dependencies |
| Jupyter / Google Colab | Interactive notebooks for testing and exploration |
| Git + GitHub | Version control and storing code remotely |

The standard setup is: write code in VS Code, manage dependencies in a virtual environment, test interactively in a notebook when needed, and push everything to GitHub.

---

## LLMs as Coding Assistants

LLMs like ChatGPT, Claude, and Gemini are trained on massive amounts of text and code. They can generate code, explain it line by line, suggest fixes, and help you understand error messages. They enable a top-down learning approach: start by building something, then learn the concepts underneath as you go.

That said, LLMs make mistakes. They can generate plausible-looking but broken code, miss recent library updates, and introduce security issues. You're still the one steering. Always read, run, and understand any code before using it.

---

## Key Takeaways

1. Programming is about breaking problems into precise steps a computer can follow.
2. The Plan → Code → Test → Refine cycle applies at every skill level.
3. Python is beginner-friendly and dominates the AI space.
4. Master the fundamentals: variables, data types, data structures, control flow, functions.
5. Use LLMs to accelerate learning, but verify everything they produce.
6. Set up proper tooling early: VS Code, pip, virtual environments, Git.

---

## Resources

- [Blog: Learning AI Engineering Backwards (On Purpose)](https://garretos.github.io/posts/learning-ai-engineering-backwards-on-purpose/)
- [Video: Course Intro](https://www.youtube.com/watch?v=_hOpfENqPPA)
- [Video: How LLMs Can Be Used as Coding Assistants](https://www.youtube.com/watch?v=F1COwAB_g_E)
- [Video: CS Fundamentals](https://www.youtube.com/watch?v=_uRb5wlFhyw)
- NotebookLM notes (saved locally)
