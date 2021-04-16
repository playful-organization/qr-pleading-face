import qrcode
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=["GET"])
def get():
    text = request.args.get("t")
    qr = qrcode.QRCode()
    qr.add_data(text)
    qr.make()
    matrix = qr.get_matrix() if text else []
    return render_template('index.html', matrix=matrix, text=text)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
