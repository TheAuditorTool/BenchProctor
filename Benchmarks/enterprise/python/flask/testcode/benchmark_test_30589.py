# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request
from app_runtime import db


def BenchmarkTest30589():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if comment_value:
        data = comment_value
    else:
        data = ''
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
