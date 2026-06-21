# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify


def BenchmarkTest65106():
    cookie_value = request.cookies.get('session_token', '')
    Fernet(cookie_value.encode() if isinstance(cookie_value, str) else cookie_value).encrypt(b'data')
    return jsonify({"result": "success"})
