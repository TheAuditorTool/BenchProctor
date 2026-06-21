# SPDX-License-Identifier: Apache-2.0
import jwt
import keyring
from flask import jsonify


def BenchmarkTest14446():
    secret_value = 'app_display_name'
    data = (lambda v: v.strip())(secret_value)
    store_cred = keyring.get_password('app', 'service-account')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return jsonify({"result": "success"})
