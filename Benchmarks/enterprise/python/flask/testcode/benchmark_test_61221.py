# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request
from app_runtime import db


def BenchmarkTest61221():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(comment_value)).read()
    return jsonify({"result": "success"})
