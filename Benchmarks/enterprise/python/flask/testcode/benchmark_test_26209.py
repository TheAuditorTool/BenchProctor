# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify


def BenchmarkTest26209():
    host_value = request.headers.get('Host', '')
    Fernet(host_value.encode() if isinstance(host_value, str) else host_value).encrypt(b'data')
    return jsonify({"result": "success"})
