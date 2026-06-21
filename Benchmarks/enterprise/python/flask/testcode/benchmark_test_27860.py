# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest27860():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        return jsonify({'error': 'privilege drop failed'}), 500
    return jsonify({"result": "success"})
