# SPDX-License-Identifier: Apache-2.0
import jwt
import keyring
from flask import jsonify


def BenchmarkTest00561():
    secret_value = 'feature_flag_value'
    data = f'{secret_value:.200s}'
    store_cred = keyring.get_password('app', 'service-account')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return jsonify({"result": "success"})
