import os

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/map")
def map():
    return render_template('index.html')


def run():
    port = 80
    while 1:
        try:
            app.run(host='0.0.0.0', port=port, debug=True)
            break
        except OSError:
            port += 1
        except Exception as e:
            print(e)
            break

if __name__ == '__main__':
    run()
