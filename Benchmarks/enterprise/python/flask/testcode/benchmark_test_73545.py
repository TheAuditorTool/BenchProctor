# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import time
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest73545():
    header_value = request.headers.get('X-Custom-Header', '')
    data = handle(header_value)
    if time.time() > 1000000000:
        _resp = requests.get(str(data))
        db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return jsonify({"result": "success"})
