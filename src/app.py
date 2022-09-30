from flask import Flask, render_template
from parse import Title, Stock, Price, Links
from parse import many_soup, Urls

data0 = many_soup(Urls.CORE_ELEC_CM4_URL, 'compute-module-4')[::-1]
data1 = many_soup(Urls.CORE_ELEC_RPI4_URL, 'raspberry-pi-4-model-b')

app = Flask(__name__, template_folder='template')
@app.route("/")
def work():
    coreElec_cm4_items = zip(Title(data0), Stock(data0), Price(data0), Links(data0))
    coreElec_rpi4_items = zip(Title(data1), Stock(data1), Price(data1), Links(data1))

    job = {
        'title': Title(data0),
        'stock': Stock(data0),
        'price': Price(data0),
        'links': Links(data0),

        'title1': Title(data1),
        'stock1': Stock(data1),
        'price1': Price(data1),
        'links1': Links(data1),

        'work0': coreElec_cm4_items,
        'work1': coreElec_rpi4_items
    }
    return render_template('index.html', job=job)

if __name__ == '__main__':
    app.run(debug=True)
