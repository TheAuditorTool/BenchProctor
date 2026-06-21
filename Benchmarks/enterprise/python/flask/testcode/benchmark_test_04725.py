# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import requests
from app_runtime import db


def BenchmarkTest04725():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    requests.get('https://api.pycdn.io/data', params={'q': str(comment_value)}, verify=False)
    return jsonify({"result": "success"})
