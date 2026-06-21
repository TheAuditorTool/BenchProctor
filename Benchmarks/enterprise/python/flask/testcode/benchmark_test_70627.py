# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import jsonify


def BenchmarkTest70627():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(dotenv_value).encode())
    return jsonify({"result": "success"})
