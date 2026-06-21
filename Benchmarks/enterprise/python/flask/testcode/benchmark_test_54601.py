# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest54601():
    secret_value = ['s3cr3t_key_test_xyz'][0]
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
