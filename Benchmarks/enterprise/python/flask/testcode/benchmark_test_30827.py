# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from app_runtime import db


def BenchmarkTest30827():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    requests.post('http://api.prod.internal/data', data=str(db_value))
    return jsonify({"result": "success"})
