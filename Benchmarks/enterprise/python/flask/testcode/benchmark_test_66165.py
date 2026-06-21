# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import json
from app_runtime import db


def BenchmarkTest66165():
    secret_value = 'feature_flag_value'
    try:
        data = json.loads(secret_value).get('value', secret_value)
    except (json.JSONDecodeError, AttributeError):
        data = secret_value
    store_cred = os.environ.get('APP_SECRET', '')
    db.connect(host='localhost', user=str(data), password=store_cred)
    return jsonify({"result": "success"})
