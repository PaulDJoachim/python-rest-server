from flask import render_template
from app import app


@app.route('/')
def index():
    user = {'username': 'Paul'}
    return render_template('index.html', title='Home', user=user)

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

# if __name__ == '__main__':
#     app.run()