# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import keyring
from flask import jsonify


def BenchmarkTest58981():
    secret_value = 'default_config_label'
    parts = []
    for token in str(secret_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
