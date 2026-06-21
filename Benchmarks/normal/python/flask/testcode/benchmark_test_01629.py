# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from cryptography.fernet import Fernet
from dataclasses import dataclass
from flask import jsonify
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest01629(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode()).decode()
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', encrypted, secure=True, httponly=True, samesite='Strict')
    return resp
