# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import json
from app_runtime import db


def BenchmarkTest36706():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = json.loads(comment_value).get('value', comment_value)
    except (json.JSONDecodeError, AttributeError):
        data = comment_value
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
