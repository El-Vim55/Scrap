from flask import Flask, render_template
from parse import Title, Stock, Price, Links

app = Flask(__name__, template_folder='template')
@app.route("/")

def work():
    """ when the site is ready to have a domain, the below code will be used to automate the tables"""
    coreElectronic_cm4_items = zip(Title(), Stock(), Price(), Links())

    job = {
        'title': Title(),
        'stock': Stock(),
        'price': Price(),
        'links': Links(),
        'work0': coreElectronic_cm4_items,
    }
    return render_template('del.html', job=job,)

if __name__ == '__main__':
    app.run(debug=True)
