# SPDX-License-Identifier: Apache-2.0
import re
import os
from flask import jsonify
import socket


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest20679():
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    s = socket.create_connection((str(processed), 80))
    s.close()
    return jsonify({"result": "success"})
