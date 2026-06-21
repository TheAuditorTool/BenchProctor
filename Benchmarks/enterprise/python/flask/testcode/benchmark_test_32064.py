# SPDX-License-Identifier: Apache-2.0
import requests
import base64
from flask import jsonify
from app_runtime import db


def BenchmarkTest32064():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
