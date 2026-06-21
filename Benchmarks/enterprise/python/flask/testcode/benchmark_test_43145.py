# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest43145():
    auth_header = request.headers.get('Authorization', '')
    data = handle(auth_header)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
