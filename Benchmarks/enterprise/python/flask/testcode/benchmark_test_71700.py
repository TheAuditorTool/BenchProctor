# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest71700():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    eval(str(comment_value))
    return jsonify({"result": "success"})
