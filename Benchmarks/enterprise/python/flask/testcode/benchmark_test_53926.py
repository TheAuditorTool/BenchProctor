# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def relay_value(value):
    return value

def BenchmarkTest53926():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = relay_value(secret_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
