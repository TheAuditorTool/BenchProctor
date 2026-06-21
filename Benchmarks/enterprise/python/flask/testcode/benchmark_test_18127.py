# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest18127():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
