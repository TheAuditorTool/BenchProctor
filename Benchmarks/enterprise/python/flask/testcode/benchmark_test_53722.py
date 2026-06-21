# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def BenchmarkTest53722():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode()).decode()
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', encrypted, secure=True, httponly=True, samesite='Strict')
    return resp
