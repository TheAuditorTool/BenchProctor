# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest38755():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
