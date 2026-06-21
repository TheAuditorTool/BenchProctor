# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
import pickle


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest29011():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = handle(forwarded_ip)
    if time.time() > 1000000000:
        pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
