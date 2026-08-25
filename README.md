# LAB EX29: feature-login branch + PR merge

Repo: https://github.com/JoanathanPS/Exp29

## Steps
```powershell
git checkout -b feature-login
```
Added `login.py` with a simple `login(username, password)` function backed
by an in-memory demo user store (`admin`/`admin123`, `joanathan`/`csa1016`).
```powershell
git add login.py
git commit -m "Add simple login function in login.py"
git push -u origin feature-login
```
Opened PR: **"Add login function"**, `feature-login` -> `main`:
https://github.com/JoanathanPS/Exp29/pull/1

Merged via GitHub (merge commit, not squash/rebase, to keep the branch
history visible).

## Screenshots to save here (1.png ... 5.png, max 5)
1. `login.py` contents / editor view.
2. PR #1 page showing `feature-login` -> `main`.
3. `git push` output showing the branch pushed.
4. PR #1 after merge (green "Merged" badge).
5. `main` branch on GitHub now containing `login.py`.
