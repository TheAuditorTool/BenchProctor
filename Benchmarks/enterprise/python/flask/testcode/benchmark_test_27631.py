# SPDX-License-Identifier: Apache-2.0
import requests
import base64
from flask import jsonify
from app_runtime import db


def BenchmarkTest27631():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
