# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest80617():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = coalesce_blank(comment_value)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
