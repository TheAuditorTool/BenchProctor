# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import os


def BenchmarkTest51266():
    secret_value = 'default_setting_value'
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(secret_value)
    data = collected
    Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
