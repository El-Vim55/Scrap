from flask import Flask, render_template
import json
from parse import Title, Stock, Price, Links

app = Flask(__name__, template_folder='template')

@app.route("/")
def work():
    job = {
        'title': Title(),
        'stock': Stock(),
        'price': Price(),
        'links': Links()
    }
    return render_template('index.html', job=job)

if __name__ == '__main__':
    app.run(debug=True)
