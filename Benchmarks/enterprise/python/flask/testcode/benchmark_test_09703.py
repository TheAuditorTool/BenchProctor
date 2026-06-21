# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def BenchmarkTest09703():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data, _sep, _rest = str(secret_value).partition('\x00')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
