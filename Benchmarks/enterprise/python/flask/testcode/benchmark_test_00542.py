# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest00542():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
