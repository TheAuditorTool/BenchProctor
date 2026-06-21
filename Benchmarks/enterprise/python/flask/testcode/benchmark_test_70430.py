# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest70430():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    os.remove(str(data))
    return jsonify({"result": "success"})
