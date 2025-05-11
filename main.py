from flask import *

app = Flask(__name__)

@app.route('/')
def homepage():
    #ill use jinja2 templates idrk lmao
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)