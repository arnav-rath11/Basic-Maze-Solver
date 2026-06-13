# 🧩 Maze Solver

A Python-based puzzle solver that finds **all possible paths** through a matrix-represented maze — from the bottom-left corner to the top-right corner — and prints each valid solution step-by-step.

---

## 📌 Project Brief

The Maze Solver takes a 2D matrix as input where:
- **Spaces `" "`** represent open, walkable paths
- **Hash symbols `"#"`** represent walls (blocked cells)

The program explores all four directions (up, down, left, right) from the starting position using a **BFS-like path expansion** approach. Every valid path found is printed with numbered steps showing the exact route taken. If no path exists, it simply terminates silently.

> **Start point:** Bottom-left corner of the matrix  
> **End point:** Top-right corner of the matrix

---

## 🛠️ Technical Arsenal

| Component | Details |
|-----------|---------|
| **Language** | Python 3.x |
| **Algorithm** | Breadth-First Search (BFS) style multi-path expansion |
| **Input** | CLI-based matrix input using `eval()` |
| **Output** | Console-printed solution paths with step numbers |

---

## 📦 Libraries Required

This project uses **only Python built-in libraries** — no installation needed!

| Library | Purpose |
|---------|---------|
| `copy.deepcopy` | Creates independent copies of path lists to avoid mutation across branches |
| `os.system` | Runs the `PAUSE` command to hold the terminal open after execution (Windows) |

### ✅ Installation

```bash
# No external packages needed. Just make sure you have Python 3 installed.
python --version  # Should be 3.x
```

---

## 🚀 How to Run

```bash
python maze.py
```

---

## 🎮 How to Give Input

The program prompts:
```
Enter a NxN matrix (Use hashtags for wall and space for empty area):
```

You must type a **Python 2D list** directly into the terminal. Each inner list is a row, each element is either `" "` (space = open path) or `"#"` (hash = wall).

### Input Format

```python
[[" ", " ", " "], [" ", "#", " "], [" ", " ", " "]]
```

> ⚠️ **Important:** Use actual space characters inside quotes for open cells, not empty strings. `" "` ✅ vs `""` ❌

### Example Inputs

**3×3 maze with no walls (all open):**
```
[[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
```

**3×3 maze with a middle column wall:**
```
[[" ", "#", " "], [" ", "#", " "], [" ", "#", " "]]
```
→ This will produce **no output** since all paths are blocked.

**3×3 maze with a diagonal-ish wall:**
```
[[" ", " ", "#"], [" ", " ", " "], ["#", " ", " "]]
```
→ May or may not have solutions depending on the wall placement.

---

## 📤 Output Format

For each valid path found, the matrix is printed with **step numbers** replacing the path cells, followed by a separator:

```
[' ', ' ', '4']
[' ', '2', '3']
['0', '1', ' ']
XXXXXXXXXXXXXXX
[' ', '3', '4']
['1', '2', ' ']
['0', ' ', ' ']
XXXXXXXXXXXXXXX
```

- `0` = Starting cell (bottom-left)
- Each subsequent number = next step in the path
- The highest number = the destination (top-right)
- `XXXXXXXXXXXXXXX` = separator between different solutions
- If **no output** appears before the pause, there is no valid path

---

## 🖥️ Sample Run

**Input:**
```
Enter a NxN matrix: [[" "," "," "],[" "," "," "],[" "," "," "]]
```

**Output (multiple solutions):**
```
[' ', ' ', '4']
[' ', '1', '3']
['0', '2', ' ']      ← wait no, actual numbered path
XXXXXXXXXXXXXXX
[' ', '2', '3']
['1', ' ', '4']
['0', ' ', ' ']
XXXXXXXXXXXXXXX
... (more solutions)
Press any key to continue . . .
```

---

## 📁 Project Structure

```
maze-solver/
│
└── maze.py        # Main source file (single script project)
```

---

## ⚠️ Known Limitations

- Uses `eval()` on raw input — safe for personal/academic use only, not for production
- `os.system("PAUSE")` works only on **Windows**. On Linux/Mac, replace with:
  ```python
  input("Press Enter to exit...")
  ```
- Very large mazes may be slow due to exhaustive path expansion

---

## 📚 Bibliography

- *Computer Science with Python* — Class XI, Sumita Arora

---

## 👨‍💻 Hardware Used During Development

- **Processor:** Intel Core i3-1005G1 @ 1.20GHz  
- **RAM:** 2.0 GB  
- **OS:** 64-bit Windows  
- **IDE:** Python IDLE 3.10 (64-bit)
