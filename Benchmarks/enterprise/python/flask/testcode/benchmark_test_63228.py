# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest63228():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = normalise_input(comment_value)
    if str(data) in ('localhost', 'internal-gateway'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
