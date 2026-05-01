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

# CAREERS PAGE
@app.route('/careers')
def careers():
    return render_template('careers.html')

# GALLERY PAGE
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# QUALITY AND SAFETY PAGE
@app.route('/quality-and-safety')
def quality_safety():
    return render_template('quality_safety.html')

# BOARD MEMBERS PAGE
@app.route('/board-members')
def board_members():
    return render_template('board_members.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))