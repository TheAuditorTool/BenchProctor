# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest06996():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if not str(comment_value).isdigit():
        raise ValueError('invalid input: ' + str(comment_value))
    return jsonify({"result": "success"})
