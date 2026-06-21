# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest46342():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = ' '.join(str(comment_value).split())
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
