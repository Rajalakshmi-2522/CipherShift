from flask import Flask, render_template, request
import random

app = Flask(__name__)

alphabet = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    return cipher_text

def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_key) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    return plain_text

# ---------------- GAME DATA ----------------
words = [
    ("elephant", "animal"),
    ("guitar", "musical instrument"),
    ("banana", "fruit"),
    ("python", "programming language"),
    ("tiger", "animal"),
    ("apple", "fruit"),
    ("violin", "musical instrument"),
    ("kangaroo", "animal")
]

secret_shift = None
encrypted_message = None
original_message = None
hint = None
shift_attempts = 3
message_attempts = 2
shift_found = False

@app.route("/", methods=["GET", "POST"])
def index():
    global secret_shift, encrypted_message
    global original_message, hint
    global shift_attempts, message_attempts, shift_found

    result = ""

    if request.method == "POST":
        action = request.form["action"]

        # --------- START / RESTART ---------
        if action == "start":
            min_shift = int(request.form["min_shift"])
            max_shift = int(request.form["max_shift"])

            original_message, hint = random.choice(words)
            secret_shift = random.randint(min_shift, max_shift)
            encrypted_message = encryption(original_message, secret_shift)
            
            shift_attempts = 3
            message_attempts = 2
            shift_found = False
            result = f"Game started! Hint: {hint}. Guess the shift key."

        # --------- CHECK SHIFT ---------
        elif action == "check_shift" and shift_attempts > 0:
            user_shift = int(request.form["user_shift"])

            if user_shift == secret_shift:
                result = "✅ Correct shift key found! Now decrypt the message."
                shift_found = True
            else:
                shift_attempts -= 1
                if shift_attempts > 0:
                    result = f"❌ Wrong shift key. You have {shift_attempts} attempts left."
                else:
                    result = f"💀 Out of attempts! The shift was {secret_shift} and decrypted message was '{original_message}'."

        # --------- CHECK MESSAGE ---------
        elif action == "check_message" and shift_found and message_attempts > 0:
            user_message = request.form["user_message"].lower()
            decrypted = decryption(encrypted_message, secret_shift)

            if user_message == decrypted:
                result = "🎉 SUCCESS! You won!"
            else:
                message_attempts -= 1
                if message_attempts > 0:
                    result = f"❌ Incorrect message. You have {message_attempts} attempts left."
                else:
                    result = f"💀 Out of attempts! The correct decrypted message was '{decrypted}'."

    return render_template(
        "index.html",
        encrypted_message=encrypted_message,
        result=result,
        shift_attempts=shift_attempts,
        message_attempts=message_attempts,
        shift_found=shift_found,
        hint=hint
    )

if __name__ == "__main__":
    app.run(debug=True)
 