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
    #Formda gönderilen veriler alınacak
    email = request.form.get('email')
    text = request.form.get('text')

    #.Txt dosyasına ya da veritabanına yazılacak
    with open('feedback.txt', 'a', encoding='Utf-8') as dosya:
        dosya.write(f"Email: {email}\n") #Email adresi .txtye yazıldı
        dosya.write(f"Yorum: {text}\n")
        dosya.write("-" * 50 + "\n")
        

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
