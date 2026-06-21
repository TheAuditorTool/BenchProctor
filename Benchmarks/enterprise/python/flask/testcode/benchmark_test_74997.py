# SPDX-License-Identifier: Apache-2.0
import jwt
import os
from flask import jsonify


def BenchmarkTest74997():
    secret_value = 'default_setting_value'
    data = ' '.join(str(secret_value).split())
    store_cred = os.environ.get('APP_SECRET', '')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return jsonify({"result": "success"})
