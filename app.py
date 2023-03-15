from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def kalkpaliwa():
    #Scrapowanie cen paliwa
    s = str(requests.get('https://www.autocentrum.pl/paliwa/ceny-paliw/').content)
    s = s.split('price">')
    cenyPaliwa = {}
    for x in range(1, 6):
        temp = s[x]
        temp = temp[2:]
        temp = temp.lstrip()
        temp = temp[0:4]
        cenyPaliwa[x] = temp
    #Odsłyanie strony
    if request.method == 'POST':
        #Pobieranie danych z formularza
        dystans = float(request.form['dystans'])
        srednieSpalanie = float(request.form['srednieSpalanie'])
        cenaPaliwa = float(request.form['cenaPaliwa'])

        #Obliczanie kosztu
        kosztPrzejazdu = ((srednieSpalanie*dystans)/100)*cenaPaliwa
        kosztPrzejazdu = round(kosztPrzejazdu, 2)

        return render_template('kalkpaliwa.html', dystans = dystans, srednieSpalanie = srednieSpalanie, cenaPaliwa = cenaPaliwa, kosztPrzejazdu = kosztPrzejazdu, cenyPaliwa = cenyPaliwa, proxies = proxies)
    else:
        return render_template('kalkpaliwa.html', cenyPaliwa = cenyPaliwa, proxies = proxies)


if __name__ == "__main__":
    app.run()
