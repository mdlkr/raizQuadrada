from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    num = float(request.form['numero'])
    raiz_quadrada = num ** 0.5
    return render_template('result.html', num=num, raiz_quadrada=raiz_quadrada)

if __name__ == '__main__':
    app.run()