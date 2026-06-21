# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify


def BenchmarkTest24590():
    origin_value = request.headers.get('Origin', '')
    Fernet(origin_value.encode() if isinstance(origin_value, str) else origin_value).encrypt(b'data')
    return jsonify({"result": "success"})
