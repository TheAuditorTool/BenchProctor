# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import json
from app_runtime import auth_check


def BenchmarkTest11057():
    secret_value = 'app_display_name'
    try:
        data = json.loads(secret_value).get('value', secret_value)
    except (json.JSONDecodeError, AttributeError):
        data = secret_value
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
