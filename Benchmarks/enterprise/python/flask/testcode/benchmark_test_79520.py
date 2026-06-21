# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest79520():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    prefix = ''
    data = prefix + str(comment_value)
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
