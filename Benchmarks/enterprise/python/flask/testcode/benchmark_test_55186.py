# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import json
from flask import request, jsonify
import os


def BenchmarkTest55186():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    enc_key = os.environ['DATA_ENC_KEY']
    key_expires_at = 1577836800
    if key_expires_at > 0:
        Fernet(enc_key.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
