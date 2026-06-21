# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import json
from app_runtime import db


def BenchmarkTest74629():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = json.loads(db_value).get('value', db_value)
    except (json.JSONDecodeError, AttributeError):
        data = db_value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
