# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest18188():
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
