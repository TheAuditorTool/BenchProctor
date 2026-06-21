# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def BenchmarkTest16417():
    header_value = request.headers.get('X-Custom-Header', '')
    data = bytes.fromhex(header_value).decode('utf-8', 'ignore')
    key = os.environ['DATA_ENC_KEY'].encode()
    globals().setdefault('_secret_cache', {})['current'] = Fernet(key).encrypt(str(data).encode())
    return jsonify({"result": "success"})
