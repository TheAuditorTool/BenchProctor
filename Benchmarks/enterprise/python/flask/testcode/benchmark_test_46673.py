# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request
from app_runtime import db


def BenchmarkTest46673():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = str(db_value).split(',')
    data = ','.join(parts)
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
