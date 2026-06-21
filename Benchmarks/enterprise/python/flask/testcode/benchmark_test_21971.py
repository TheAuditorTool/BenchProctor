# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import requests
from app_runtime import db


def BenchmarkTest21971():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = ' '.join(str(db_value).split())
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
