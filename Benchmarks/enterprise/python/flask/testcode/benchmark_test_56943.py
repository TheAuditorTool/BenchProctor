# SPDX-License-Identifier: Apache-2.0
import jwt
import keyring
from flask import jsonify


def BenchmarkTest56943():
    secret_value = 'app_display_name'
    data = f'{secret_value:.200s}'
    store_cred = keyring.get_password('app', 'service-account')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return jsonify({"result": "success"})
