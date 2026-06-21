# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from cryptography.fernet import Fernet
from urllib.parse import unquote
from flask import request, jsonify
import os


def BenchmarkTest67854():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode()).decode()
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', encrypted, secure=True, httponly=True, samesite='Strict')
    return resp
