# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest42210():
    raw_body = request.get_data(as_text=True)
    data = handle(raw_body)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(processed),))
    return jsonify({'secret': str(secret)}), 200
