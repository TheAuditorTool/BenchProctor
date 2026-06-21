# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import os


def BenchmarkTest45155():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(dotenv_value)
    data = collected
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
