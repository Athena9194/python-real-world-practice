from flask import Flask, request, redirect
from logic import save_url, url_storage
from utils import generate_short_code
app = Flask(__name__)


@app.route('/')
def home():
    return "Server is up and running!"


@app.route('/shorten')
def shorten_link():
    long_url = request.args.get('url')
    if not long_url:
        return "Error: Missing url parameter", 400

    code = save_url(long_url)
    return {
        "short_url": f"http://127.0.0.1:5000/{code}",
        "original_url": long_url
    }


@app.route('/<short_code>')
def redirect_to_original(short_code):
    if short_code in url_storage:
        return redirect(url_storage[short_code]["url"])
    return "URL not found", 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)