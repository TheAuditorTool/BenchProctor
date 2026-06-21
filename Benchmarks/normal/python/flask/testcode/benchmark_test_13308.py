# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from app_runtime import db


def BenchmarkTest13308():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = bytes.fromhex(db_value).decode('utf-8', 'ignore')
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
