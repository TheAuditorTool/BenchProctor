# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest02308():
    referer_value = request.headers.get('Referer', '')
    data = handle(referer_value)
    if str(data).lower() not in ('true', 'false'):
        return jsonify({'error': 'invalid boolean'}), 400
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
