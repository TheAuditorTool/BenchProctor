# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify


def BenchmarkTest10853():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    def normalize(value):
        return value.strip()
    data = normalize(json_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
