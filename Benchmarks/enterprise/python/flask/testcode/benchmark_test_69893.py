# SPDX-License-Identifier: Apache-2.0
import requests
import re
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest69893():
    user_id = request.args.get('id', '')
    data = handle(user_id)
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    requests.get(str(processed))
    return jsonify({"result": "success"})
