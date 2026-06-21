# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
from flask import jsonify
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest57942():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
