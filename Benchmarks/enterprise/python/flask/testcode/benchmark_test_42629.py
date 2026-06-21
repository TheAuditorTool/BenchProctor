# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import os


def BenchmarkTest42629():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = str(dotenv_value).replace('\x00', '')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
