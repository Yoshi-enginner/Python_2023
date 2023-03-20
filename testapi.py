from flask import Flask, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/generate_qr', methods=['GET'])
def generate_qr():
    url = request.args.get('url')
    if url:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')
        file_object = BytesIO()
        img.save(file_object, 'PNG')
        file_object.seek(0)
        return send_file(file_object, mimetype='image/PNG', as_attachment=True, attachment_filename='qr_code.png')
    else:
        return 'Invalid URL'

if __name__ == '__main__':
    app.run(debug=True)






