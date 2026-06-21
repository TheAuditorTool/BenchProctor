# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest30280():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
