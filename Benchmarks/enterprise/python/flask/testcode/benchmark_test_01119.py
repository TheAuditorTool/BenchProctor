# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def BenchmarkTest01119():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = ' '.join(str(secret_value).split())
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
