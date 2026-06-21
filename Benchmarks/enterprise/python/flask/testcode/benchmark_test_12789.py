# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest12789():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = ensure_str(dotenv_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
