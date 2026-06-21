# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import jsonify
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest38325():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
