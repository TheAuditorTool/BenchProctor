# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import os


def BenchmarkTest71597():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    Fernet(dotenv_value.encode() if isinstance(dotenv_value, str) else dotenv_value).encrypt(b'data')
    return jsonify({"result": "success"})
