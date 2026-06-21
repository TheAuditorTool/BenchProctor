# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import os


def BenchmarkTest31845():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    if dotenv_value:
        data = dotenv_value
    else:
        data = ''
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
