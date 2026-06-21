# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import keyring
from flask import jsonify


def relay_value(value):
    return value

def BenchmarkTest42502():
    secret_value = 'default_config_label'
    data = relay_value(secret_value)
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
