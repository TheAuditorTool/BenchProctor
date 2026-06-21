# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import keyring
from flask import jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest62699():
    secret_value = 'feature_flag_value'
    data = default_blank(secret_value)
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
