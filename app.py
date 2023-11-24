from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('input.html')


@app.route('/hello')
def about():
    return "Hello, " + request.args['name']


if __name__ == '__main__':
    app.run(debug=True)
