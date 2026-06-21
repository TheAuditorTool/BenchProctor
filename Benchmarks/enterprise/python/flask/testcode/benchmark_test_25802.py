# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def BenchmarkTest25802():
    header_value = request.headers.get('X-Custom-Header', '')
    prefix = ''
    data = prefix + str(header_value)
    enc_key = os.environ['DATA_ENC_KEY']
    key_expires_at = 1577836800
    if key_expires_at > 0:
        Fernet(enc_key.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
