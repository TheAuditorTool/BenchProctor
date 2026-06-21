# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request
from app_runtime import db


def BenchmarkTest03170():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if db_value:
        data = db_value
    else:
        data = ''
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
