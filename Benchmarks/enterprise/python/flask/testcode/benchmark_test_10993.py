# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import jsonify


def BenchmarkTest10993():
    secret_value = 'app_display_name'
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(secret_value).encode())
    return jsonify({"result": "success"})
