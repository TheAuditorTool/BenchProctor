# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import json
from app_runtime import db


def BenchmarkTest06455():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    try:
        data = json.loads(secret_value).get('value', secret_value)
    except (json.JSONDecodeError, AttributeError):
        data = secret_value
    db.connect(host='localhost', user='app', password=data)
    return jsonify({"result": "success"})
