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

def BenchmarkTest04974():
    xml_value = request.get_data(as_text=True)
    data = handle(xml_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    requests.post('http://api.prod.internal/data', data=str(processed))
    return jsonify({"result": "success"})
