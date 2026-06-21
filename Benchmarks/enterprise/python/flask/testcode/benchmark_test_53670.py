# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import keyring
import os
from flask import jsonify
import json


def BenchmarkTest53670():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
