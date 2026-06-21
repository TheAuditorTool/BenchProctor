# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import json
import socket
from app_runtime import db


def BenchmarkTest01098():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = json.loads(comment_value).get('value', comment_value)
    except (json.JSONDecodeError, AttributeError):
        data = comment_value
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
