# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest14772():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = normalise_input(comment_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
