# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import json
from flask import request, jsonify
import os


def BenchmarkTest57737():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    key = os.environ['DATA_ENC_KEY'].encode()
    globals().setdefault('_secret_cache', {})['current'] = Fernet(key).encrypt(str(data).encode())
    return jsonify({"result": "success"})
