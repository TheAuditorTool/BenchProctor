# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from app_runtime import db


def BenchmarkTest22086():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    requests.post('http://api.prod.internal/data', data=str(comment_value))
    return jsonify({"result": "success"})
