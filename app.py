from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/getdata', methods=['POST'])
def get_data():
    # get the data_source
    data_source = request.form['ds']

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
