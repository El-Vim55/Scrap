from flask import Flask, render_template
import json
from parse import parse_content

app = Flask(__name__, template_folder='template')

@app.route("/")
def work():
    return render_template('index.html')

# print(work())

if __name__ == '__main__':
    app.run(debug=True)
