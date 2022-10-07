import math, random
from AppConfig.DBConnector import get_connection
from twilio.rest import Client
from AppConfig.Keys import *


def generate_otp(language, patient_id):
    digits = "0123456789"
    code = ""
    for i in range(6):
        code += digits[math.floor(random.random() * 10)]
    otp = code
    try:
        cur, conn = get_connection()
        print('connected to database otp ')
        command = f"INSERT INTO otps (value , patient_id ) VALUES ({otp},{patient_id})"
        cur.execute(command)
        conn.commit()

    except Exception as e:
        print('generating new otp failed ', e)


def build_message(language, patient_id):
    generate_otp(language, patient_id)
    try:
        cur, conn = get_connection()
        print('connected to database')
        command = f"select message from Messages where title = 'otp_content' and language = '{language}';"
        cur.execute(command)
        res = cur.fetchone()
        body = str(res[0])
        command = f"select value from otps where patient_id = {patient_id};"
        cur.execute(command)
        res = cur.fetchone()
        code = str(res[0])
        print('code ='+code)
        print('body = '+body)
        body = body.replace('{otp}',code)
        print(body)
        return body

    except Exception as e:
        print('building patient failed ', e)


def send_otp(id, phone_number, language):
    otp = build_message(language, id)
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=otp,
        from_=twilio_number,
        to=phone_number
    )

    print(message.body)

    return message.body
