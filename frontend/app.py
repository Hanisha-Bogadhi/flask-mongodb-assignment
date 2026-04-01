from flask import Flask, render_template, request, redirect
import requests

BACKEND_URL = 'http://0.0.0.0:5000'
app = Flask(__name__) #created a flask application

@app.route('/') #creating a route
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    try:
        signup_data = dict(request.form)
        print(signup_data)  # debug
    
        requests.post(BACKEND_URL + '/signup', json=signup_data)
    
        return redirect('/success')
    except Exception as e:
        return render_template('index.html', error=str(e))

@app.route('/success')
def success():
     return render_template('success.html')

if __name__ == '__main__': #calling function

   app.run(host='0.0.0.0', port=4000, debug=True) #to update changes automatically
