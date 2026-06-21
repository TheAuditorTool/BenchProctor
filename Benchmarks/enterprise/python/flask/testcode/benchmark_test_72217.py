# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import urllib.request
from app_runtime import db


def BenchmarkTest72217():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', comment_value):
        return jsonify({'error': 'forbidden'}), 400
    processed = comment_value
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return jsonify({"result": "success"})
