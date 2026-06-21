# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import json
import os


def BenchmarkTest04250():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    try:
        data = json.loads(dotenv_value).get('value', dotenv_value)
    except (json.JSONDecodeError, AttributeError):
        data = dotenv_value
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
