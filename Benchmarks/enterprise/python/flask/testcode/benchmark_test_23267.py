# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify
from app_runtime import db


def BenchmarkTest23267():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = comment_value if comment_value else 'default'
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
