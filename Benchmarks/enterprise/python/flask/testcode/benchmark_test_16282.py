# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify
from app_runtime import db


def BenchmarkTest16282():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data, _sep, _rest = str(comment_value).partition('\x00')
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
