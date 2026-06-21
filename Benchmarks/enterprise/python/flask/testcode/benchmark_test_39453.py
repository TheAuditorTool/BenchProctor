# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import urllib.request
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest39453():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return jsonify({"result": "success"})
