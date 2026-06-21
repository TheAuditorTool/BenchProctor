# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import os


def BenchmarkTest32837():
    secret_value = 'app_display_name'
    Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(secret_value).encode())
    return jsonify({"result": "success"})
