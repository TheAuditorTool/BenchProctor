# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
import urllib.request
from app_runtime import db


def BenchmarkTest00586():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = json.loads(comment_value).get('value', comment_value)
    except (json.JSONDecodeError, AttributeError):
        data = comment_value
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
