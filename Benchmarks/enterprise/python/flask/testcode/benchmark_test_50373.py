# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import json
from app_runtime import auth_check


def BenchmarkTest50373():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    try:
        data = json.loads(file_value).get('value', file_value)
    except (json.JSONDecodeError, AttributeError):
        data = file_value
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
