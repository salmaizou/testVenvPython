from flask import Flask
app = Flask(__name__)

@app.route("/")

def accueil():
     return "Ismail m'a enguelé cet aprem et je suis pas contente"

if __name__ == "__main__":
     app.run(debug=True)
