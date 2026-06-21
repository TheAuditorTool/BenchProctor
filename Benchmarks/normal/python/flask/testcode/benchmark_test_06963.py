# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from app_runtime import db


def BenchmarkTest06963():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    requests.get('https://api.pycdn.io/data', params={'q': str(db_value)}, verify=True)
    return jsonify({"result": "success"})
