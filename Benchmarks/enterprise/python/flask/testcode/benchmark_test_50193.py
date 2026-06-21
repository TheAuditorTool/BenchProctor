# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
from app_runtime import db


def BenchmarkTest50193():
    origin_value = request.headers.get('Origin', '')
    try:
        data = json.loads(origin_value).get('value', origin_value)
    except (json.JSONDecodeError, AttributeError):
        data = origin_value
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return jsonify({"result": "success"})
