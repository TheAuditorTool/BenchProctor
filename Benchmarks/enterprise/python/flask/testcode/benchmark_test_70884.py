# SPDX-License-Identifier: Apache-2.0
import jwt
import os
from flask import jsonify


def BenchmarkTest70884():
    secret_value = 'app_display_name'
    data = str(secret_value).replace('\x00', '')
    store_cred = os.environ.get('APP_SECRET', '')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return jsonify({"result": "success"})
