# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import jsonify


def BenchmarkTest80568():
    env_value = os.environ.get('USER_INPUT', '')
    Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(env_value).encode())
    return jsonify({"result": "success"})
