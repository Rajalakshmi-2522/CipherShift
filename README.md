# <h1 align="center">🎮 Caesar Cipher Challenge Game</h1>

 An interactive **Caesar Cipher Puzzle Game** built using **Python (Flask)**.  
This game challenges players to **crack an encrypted message** by finding the correct shift key within limited attempts.

---

## 🧩 Game Concept

Unlike a normal Caesar Cipher tool, this project works as a **game**:

- The **player selects a shift key range** (minimum and maximum)
- The **computer randomly chooses** a secret shift key from that range
- A **random encrypted word** is generated
- A **hint** is provided
- The player must **guess the shift key** and **decrypt the message**
- The goal is to solve it in **fewer chances**

---

## 🕹️ How the Game Works

1. Player enters:
   - Minimum shift key
   - Maximum shift key
2. Computer:
   - Selects a random shift key
   - Generates an encrypted word
3. Game displays:
   - Encrypted message
   - Hint
4. Player:
   - Tries different keys
   - Decrypts the message
5. Game ends when:
   - Correct key is found ✅  
   - Or chances are exhausted ❌

---

## 🧠 Example Gameplay

| Step | Description |
|----|----|
| Key Range | 2 – 8 |
| Secret Key | Random (chosen by computer) |
| Encrypted Word | `KHOOR` |
| Hint | Common greeting |
| Player Guess | Shift = 3 |
| Result | 🎉 Correct! |

---

## 🎯 Game Rules

- Shift key is always within the selected range
- Alphabet wraps around (Z → A)
- Fewer attempts = better score
- Player must think logically using the hint

---

## ✨ Features

- Random shift key generation
- Random encrypted words
- Hint-based puzzle solving
- Limited attempts system
- Interactive web gameplay
- Beginner-friendly UI

---

## 🛠️ Tech Stack

- **Python**
- **Flask**
- **HTML**
- **CSS**
- **JavaScript**

---

## ⚙️ Core Logic (Behind the Scenes)

- Random number generation for shift key
- Caesar Cipher encryption algorithm
- User input validation
- Attempt tracking
- Win / lose condition handling

---

## 🚀 Run the Game Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/CipherShift.git
