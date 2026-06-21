# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
import urllib.request
from app_runtime import db


def BenchmarkTest11528():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
