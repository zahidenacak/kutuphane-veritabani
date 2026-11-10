from flask import Flask

app = Flask(__name__)

@app.route("/")
def anasayfa():
    return "Sistem başarıyla çalışıyor! Adım 7 deneme."

if __name__ == "__main__":
    app.run(debug=True)