# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import json
from app_runtime import db


def BenchmarkTest14821():
    secret_value = 'config_secret_test_abc123'
    try:
        data = json.loads(secret_value).get('value', secret_value)
    except (json.JSONDecodeError, AttributeError):
        data = secret_value
    db.connect(host='localhost', user='app', password=data)
    return jsonify({"result": "success"})
