# SPDX-License-Identifier: Apache-2.0
import requests
import json
from flask import jsonify
from app_runtime import db


def BenchmarkTest67465():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
