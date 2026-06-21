# SPDX-License-Identifier: Apache-2.0
import requests
import json
from flask import jsonify
from app_runtime import db


def BenchmarkTest13847():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
