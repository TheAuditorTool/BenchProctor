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

def BenchmarkTest28661():
    field_value = request.form.get('field', '')
    data = handle(field_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
