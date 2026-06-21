# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest79924():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
