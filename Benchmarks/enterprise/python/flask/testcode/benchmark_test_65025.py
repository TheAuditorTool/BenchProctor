# SPDX-License-Identifier: Apache-2.0
import jwt
import os
from flask import jsonify


def BenchmarkTest65025():
    secret_value = 'default_setting_value'
    data = '%s' % str(secret_value)
    store_cred = os.environ.get('APP_SECRET', '')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return jsonify({"result": "success"})
