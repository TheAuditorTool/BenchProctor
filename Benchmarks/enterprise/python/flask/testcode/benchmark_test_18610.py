# SPDX-License-Identifier: Apache-2.0
import requests
import re
from flask import jsonify
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest18610():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = relay_value(comment_value)
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    requests.get(str(processed))
    return jsonify({"result": "success"})
