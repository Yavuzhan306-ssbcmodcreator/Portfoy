# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Form işleme
@app.route('/', methods=['POST'])
def process_form():
    # Buraya kodunuzu yazın
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
