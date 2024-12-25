from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
def home():
    return render_template('live_listen.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)