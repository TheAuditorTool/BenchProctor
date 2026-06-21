# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
import urllib.request
from app_runtime import db


def BenchmarkTest11480():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
