# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest48740():
    cookie_value = request.cookies.get('session_token', '')
    data = to_text(cookie_value)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
