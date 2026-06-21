# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import keyring
from flask import jsonify


def BenchmarkTest41887():
    secret_value = 'app_display_name'
    data = str(secret_value).replace('\x00', '')
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
