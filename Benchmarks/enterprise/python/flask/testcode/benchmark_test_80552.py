# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify
from app_runtime import db


def BenchmarkTest80552():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if comment_value:
        data = comment_value
    else:
        data = ''
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
