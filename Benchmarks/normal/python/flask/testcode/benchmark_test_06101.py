# SPDX-License-Identifier: Apache-2.0
import re
import os
from flask import jsonify
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest06101():
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    if not re.fullmatch("^[\\w\\s.'\\\\;_/\\-]+$", data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return jsonify({"result": "success"})
