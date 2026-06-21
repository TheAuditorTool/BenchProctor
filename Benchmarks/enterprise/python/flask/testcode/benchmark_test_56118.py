# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import os


def BenchmarkTest56118():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(dotenv_value)
    data = collected
    Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
