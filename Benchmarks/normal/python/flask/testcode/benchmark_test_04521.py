# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def BenchmarkTest04521():
    cookie_value = request.cookies.get('session_token', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(cookie_value).encode())
    return jsonify({'length': len(ciphertext)}), 200
