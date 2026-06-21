# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from urllib.parse import unquote
from flask import request, jsonify
import os


def BenchmarkTest37812():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    enc_key = os.environ['DATA_ENC_KEY']
    key_expires_at = 1577836800
    if key_expires_at > 0:
        Fernet(enc_key.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
