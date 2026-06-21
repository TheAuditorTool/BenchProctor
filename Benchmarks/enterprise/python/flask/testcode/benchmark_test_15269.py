# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import os


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest15269():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = default_blank(dotenv_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
