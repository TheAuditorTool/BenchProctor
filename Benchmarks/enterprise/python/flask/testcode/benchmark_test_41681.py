# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify


def BenchmarkTest41681():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    Fernet(json_value.encode() if isinstance(json_value, str) else json_value).encrypt(b'data')
    return jsonify({"result": "success"})
