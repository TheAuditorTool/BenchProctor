# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import keyring
import os
from flask import jsonify


def BenchmarkTest76641():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
