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

def BenchmarkTest71973():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    data = handle(query_array)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
