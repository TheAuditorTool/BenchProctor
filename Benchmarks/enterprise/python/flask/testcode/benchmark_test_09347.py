# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import json
from flask import request, jsonify
import os


def BenchmarkTest09347():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    enc_key = os.environ['DATA_ENC_KEY']
    key_expires_at = 1577836800
    if key_expires_at > 0:
        Fernet(enc_key.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
