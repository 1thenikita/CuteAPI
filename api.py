from flask import Flask, redirect
import requests

from flask_httpauth import HTTPBasicAuth

app = Flask(__name__, static_url_path="")
auth = HTTPBasicAuth()

@app.route('/gif/cute')
def get_cute_gif():
    r = requests.get("https://evergene.io/api/hug}")
    r.json()['url']
    return redirect(r.json()['url'], code=302)


if __name__ == '__main__':
    global connectionAuth, connectionEco
    app.run('127.0.0.1', 80, app, use_reloader=True, use_debugger=True)