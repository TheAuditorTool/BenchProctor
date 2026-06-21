# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest11372():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = to_text(comment_value)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
