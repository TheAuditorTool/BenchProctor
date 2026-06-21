# SPDX-License-Identifier: Apache-2.0
import jwt
import keyring
from flask import jsonify


def BenchmarkTest69509():
    secret_value = 'default_config_label'
    def normalize(value):
        return value.strip()
    data = normalize(secret_value)
    store_cred = keyring.get_password('app', 'service-account')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return jsonify({"result": "success"})
