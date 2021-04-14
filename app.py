from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog/courier')
def testRoute():
    return render_template('courier.html')

@app.route('/blog/amd')
def amd():
    return render_template('amd.html')

if __name__ == '__main__':
    app.run(debug=True)