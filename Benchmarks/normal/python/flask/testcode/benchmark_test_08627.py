# SPDX-License-Identifier: Apache-2.0
import requests
import re
from flask import jsonify
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest08627():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = default_blank(comment_value)
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    requests.get(str(processed))
    return jsonify({"result": "success"})
