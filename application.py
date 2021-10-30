from flask import Flask, render_template, request

application = Flask(__name__)


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/getdata', methods=['POST'])
def get_data():
    # get the data_source
    data_source = request.form['ds']

    return render_template('index.html')


if __name__ == "__main__":
    application.run(debug=True)
