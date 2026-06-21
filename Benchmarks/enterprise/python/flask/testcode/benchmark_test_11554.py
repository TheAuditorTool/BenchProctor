# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from app_runtime import db


def BenchmarkTest11554():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(db_value)
    data = collected
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
