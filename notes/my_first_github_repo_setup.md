# Setting Up My First GitHub Repo

I finally got my `python-ai-foundations` repository up and running, so I wanted to write down everything I did while it's fresh. This covers the full setup on Linux Mint using VS Code, Git, and GitHub, and marks the point where I stop fiddling with configuration and actually start building things.

# Creating the Repo on GitHub

I named it `python-ai-foundations` with the description: *"Exercises, notes, and projects from my Python to AI foundations learning journey."*

For settings, I made it public, added a README, selected the Python `.gitignore` template, and chose the MIT License. More on that in a second.

# Why MIT?

The MIT License is about as permissive as it gets. Anyone can use, modify, distribute, or even commercialize my code. They just have to keep the original license attached and can't hold me liable for anything. It felt like the right call for a learning project. Simple and professional.

# Cloning It Locally

From the home directory:

```bash
cd ~
git clone https://github.com/<username>/python-ai-foundations.git
cd python-ai-foundations
```

# Git Identity (One-Time Thing)

Before doing anything else, I set my global Git identity. You only need to do this once, and it doesn't matter which folder you're in:

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

# The Password Problem (and the Fix)

GitHub stopped accepting account passwords for push operations a while back. The fix is to generate a Personal Access Token, specifically a Classic token with the `repo` scope and a 90-day expiration. When Git prompts for a password, you paste the token instead. Annoying to discover the first time, easy once you know.

# Opening in VS Code

Once inside the repo folder:

```bash
code .
```

The VS Code integrated terminal and the regular Linux terminal behave identically, both run bash. I just find the VS Code one more convenient since everything's in one window.

# Folder Structure

I set up the project like this:

```
python-ai-foundations/
│
├── data/
├── exercises/
│   └── intro/
├── notes/
│   └── intro.md
├── projects/
├── scripts/
├── .gitignore
├── LICENSE
└── README.md
```

The logic: `notes/` for learning summaries, `exercises/` for small practice files, `projects/` for bigger builds, `scripts/` for helper utilities, and `data/` for small datasets only (nothing large goes in a repo).

# The Basic Git Workflow

Every time I make changes, the cycle is the same:

```
edit → save → add → commit → push
```

```bash
git add README.md
git commit -m "Update README"
git push
```

# Syncing Rules

Git doesn't sync automatically, you have to tell it what to do.

If you edited something on GitHub directly, run `git pull` locally. If you edited something locally, run `git push`. That's it.

# Errors I Hit (and What They Mean)

A few things tripped me up that are worth noting. "Everything up-to-date" just means nothing new to push, not an error. If a file isn't updating, it almost always means you forgot to save it. Authentication failures mean you need to use the token instead of your account password. And a wrong username is harmless, just retry.

When in doubt, these four commands tell you basically everything:

```bash
git status
git branch --show-current
git remote -v
git log -1 --oneline
```

# Where I'm At

The repo exists, local and remote are connected, authentication works, and the folder structure is clean. Setup is done. Time to actually write some Python.