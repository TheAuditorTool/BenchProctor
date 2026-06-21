# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from app_runtime import db


def BenchmarkTest41399():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    prefix = ''
    data = prefix + str(comment_value)
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return jsonify({"result": "success"})
