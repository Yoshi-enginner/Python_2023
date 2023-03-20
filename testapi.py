from flask import Flask, request, send_file
import qrcode
import io

app = Flask(__name__)

@app.route('/qrcode', methods=['GET'])
def generate_qr_code():
    # Get the URL from the query string
    url = request.args.get('url')

    # Generate a QR code image
    img = qrcode.make(url)

    # Save the image to a byte buffer
    img_buffer = io.BytesIO()
    img.save(img_buffer, format='PNG')
    img_buffer.seek(0)

    # Send the image back as a response
    return send_file(img_buffer, mimetype='image/png')






