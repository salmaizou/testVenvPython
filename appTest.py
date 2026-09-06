from flask import Flask
app = Flask(__name__)

@app.route("/")

def accueil():
     return "Bonjour Salma to flask"

if __name__ == "__main__":
     app.run(debug=True)
