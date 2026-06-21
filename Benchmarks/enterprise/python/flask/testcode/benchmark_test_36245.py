# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import base64
from flask import request, jsonify
import os


def BenchmarkTest36245():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    key = os.environ['DATA_ENC_KEY'].encode()
    globals().setdefault('_secret_cache', {})['current'] = Fernet(key).encrypt(str(data).encode())
    return jsonify({"result": "success"})
