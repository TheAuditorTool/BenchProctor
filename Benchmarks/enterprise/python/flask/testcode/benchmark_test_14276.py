# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from cryptography.fernet import Fernet
from flask import jsonify
import os
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest14276():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = to_text(db_value)
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode()).decode()
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', encrypted, secure=True, httponly=True, samesite='Strict')
    return resp
