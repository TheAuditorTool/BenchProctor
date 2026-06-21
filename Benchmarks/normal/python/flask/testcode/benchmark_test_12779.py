# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import requests
from app_runtime import db


def BenchmarkTest12779():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    prefix = ''
    data = prefix + str(comment_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
