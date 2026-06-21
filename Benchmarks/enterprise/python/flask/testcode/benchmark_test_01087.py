# SPDX-License-Identifier: Apache-2.0
import jwt
import keyring
from flask import jsonify
import json


def BenchmarkTest01087():
    secret_value = 'default_config_label'
    try:
        data = json.loads(secret_value).get('value', secret_value)
    except (json.JSONDecodeError, AttributeError):
        data = secret_value
    store_cred = keyring.get_password('app', 'service-account')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return jsonify({"result": "success"})
