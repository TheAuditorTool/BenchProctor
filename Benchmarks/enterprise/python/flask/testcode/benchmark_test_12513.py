# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import json
from app_runtime import auth_check


def BenchmarkTest12513(path_param):
    path_value = path_param
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
