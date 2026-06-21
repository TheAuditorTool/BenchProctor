# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def BenchmarkTest00738():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = '%s' % str(secret_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
