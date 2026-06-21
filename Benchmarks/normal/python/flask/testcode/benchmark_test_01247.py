# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest01247():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
