from flask import Flask, render_template
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

# HOME PAGE
@app.route('/')
def home():
    return render_template('index.html')

# ABOUT PAGE
@app.route('/about')
def about():
    return render_template('about.html')

# SERVICES PAGE
@app.route('/services')
def services():
    return render_template('services.html')

# INVESTORS PAGE
@app.route('/investors')
def investors():
    return render_template('investors.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))