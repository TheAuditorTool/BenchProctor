# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify


def BenchmarkTest78762():
    referer_value = request.headers.get('Referer', '')
    Fernet(referer_value.encode() if isinstance(referer_value, str) else referer_value).encrypt(b'data')
    return jsonify({"result": "success"})
