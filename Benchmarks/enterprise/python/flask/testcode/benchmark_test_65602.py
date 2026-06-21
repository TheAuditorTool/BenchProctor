# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import os


request_state: dict[str, str] = {}

def BenchmarkTest65602():
    secret_value = 'feature_flag_value'
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
