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

def BenchmarkTest07334():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = handle(json_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
