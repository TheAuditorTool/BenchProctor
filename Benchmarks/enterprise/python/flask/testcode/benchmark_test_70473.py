# SPDX-License-Identifier: Apache-2.0
import requests
import re
from flask import jsonify
from app_runtime import db


def ensure_str(value):
    return str(value)

def BenchmarkTest70473():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = ensure_str(comment_value)
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return '<script src="' + str(processed) + '"></script>', 200, {'Content-Type': 'text/html'}
