# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def BenchmarkTest52731():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    if secret_value:
        data = secret_value
    else:
        data = ''
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
