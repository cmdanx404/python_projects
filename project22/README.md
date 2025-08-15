# 🌟 3×3 Star Finder Game

A simple Python terminal game where you try to find a hidden star on a 3×3 grid.  
You only have **3 chances** — can you find it before your luck runs out? 🎯

---

## 📜 How to Play
1. The grid is a **3×3 board** filled with white boxes (⬜).
2. The star 🌟 is hidden at a random position.
3. Enter **row** and **column** numbers (0 to 2) to guess the star's location.
4. You have only **3 attempts**:
   - **❌** means the guessed cell is empty.
   - **🌟** means you found the star!
5. If you run out of chances, the star’s position will be revealed.

---

## 🖥️ Example Gameplay

```

Welcome to the 3x3 Star Finder Game!
The grid has coordinates from 0 to 2 for both row and column.
You only have 3 chances to find the star! 🌟

⬜ ⬜ ⬜
⬜ ⬜ ⬜
⬜ ⬜ ⬜
Enter row (0-2): 1
Enter column (0-2): 1
❌ No star here. You have 2 chances left.

⬜ ⬜ ⬜
⬜ ❌ ⬜
⬜ ⬜ ⬜
...

````

---

## 📦 Installation & Running

1. **Make sure you have Python 3 installed**  
   Check your version:
   ```bash
   python --version
````

2. **Download the script**
   Save the Python code as `star_finder.py`.

3. **Run the game**

   ```bash
   python star_finder.py
   ```

---

## 🛠️ Requirements

* Python 3.x
* No external libraries needed (only uses `random` module).

---

## 🎯 Future Improvements

* Add difficulty levels (bigger grids).
* Make a graphical **Tkinter** version.
* Keep track of the player’s best score.

---

## 📄 License

This project is free to use and modify for educational purposes.
