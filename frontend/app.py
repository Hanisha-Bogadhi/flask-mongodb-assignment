from flask import Flask, render_template, request, redirect, url_for
import requests


app = Flask(__name__)


BACKEND_URL = "http://127.0.0.1:5001"

# Form page
@app.route('/')
def form():
    return render_template('index.html')

# Submit form
@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = dict(request.form)

        response = requests.post(f"{BACKEND_URL}/submit", json=data)

        if response.status_code == 200:
            return redirect(url_for('success'))
        else:
            return render_template('index.html', error=response.text)

    except Exception as e:
        return render_template('index.html', error=str(e))

# Success page
@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)