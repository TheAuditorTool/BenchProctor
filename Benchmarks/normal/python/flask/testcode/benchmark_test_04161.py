# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import jsonify


def BenchmarkTest04161():
    env_value = os.environ.get('USER_INPUT', '')
    Fernet(env_value.encode() if isinstance(env_value, str) else env_value).encrypt(b'data')
    return jsonify({"result": "success"})
