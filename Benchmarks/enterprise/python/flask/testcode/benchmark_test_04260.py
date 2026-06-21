# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest04260():
    auth_header = request.headers.get('Authorization', '')
    data = normalise_input(auth_header)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
