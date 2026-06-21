# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import keyring
import os
from flask import jsonify


def BenchmarkTest11838():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
