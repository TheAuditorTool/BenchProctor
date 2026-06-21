# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import keyring
from flask import jsonify


def BenchmarkTest18358():
    secret_value = 'feature_flag_value'
    if secret_value:
        data = secret_value
    else:
        data = ''
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
