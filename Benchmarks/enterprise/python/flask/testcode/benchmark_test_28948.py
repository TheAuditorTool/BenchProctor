# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import base64
from flask import request, jsonify
import os


def BenchmarkTest28948():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
