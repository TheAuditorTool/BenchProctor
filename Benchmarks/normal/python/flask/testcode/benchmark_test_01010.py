# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import requests
from app_runtime import db


def BenchmarkTest01010():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    prefix = ''
    data = prefix + str(db_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
