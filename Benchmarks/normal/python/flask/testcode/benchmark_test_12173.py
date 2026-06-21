# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest12173():
    multipart_value = request.form.get('multipart_field', '')
    data = default_blank(multipart_value)
    enc_key = os.environ['DATA_ENC_KEY']
    key_expires_at = 1577836800
    if key_expires_at > 0:
        Fernet(enc_key.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
