from flask import Flask
import random

app = Flask(__name__)

fortunes = [
    "A beautiful, smart, and loving person will be coming into your life.",
    "Your ability for accomplishment will follow with success.",
    "Now is the time to try something new.",
    "You will travel to many exotic places in your lifetime.",
    "The fortune you seek is in another cookie.",
    "Help! I’m stuck in a fortune cookie factory!",
    "A fresh start will put you on your way.",
    "Your shoes will make you happy today.",
    "Every exit is an entry somewhere else.",
    "You are about to become $100 richer... eventually."
]

@app.route("/")
def home():
    fortune = random.choice(fortunes)
    return f"""
        <h1>🥠 Your Fortune 🥠</h1>
        <p><em>{fortune}</em></p>
        <hr>
        <p>Refresh to receive another fortune.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
