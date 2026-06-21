# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify
from app_runtime import db


def BenchmarkTest57418():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(comment_value).split(',')
    data = ','.join(parts)
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
