from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/resposta", methods=["POST"])
def resposta():
    return "<h2>✅ Comunicação com o Back-End em Python feita com sucesso!</h2>"

if __name__ == "__main__":
    app.run(debug=True)
