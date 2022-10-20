import json

from flask import Flask, request
from Service.otpService import *

app = Flask(__name__)


@app.route('/send', methods=['POST'])
def send_otp_api():
    try:
        content = request.get_json()
        id = content['id']
        phone_number = content['phone_number']
        language = content['language']
        send_otp(id, phone_number, language)
        ot = send_otp(id, phone_number, language)
        return json.dumps({'otp': ot})
    except:
        return 500


app.run(host='0.0.0.0', port=5002)
c