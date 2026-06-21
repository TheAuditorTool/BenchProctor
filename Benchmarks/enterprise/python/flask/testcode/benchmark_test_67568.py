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

def BenchmarkTest67568():
    user_id = request.args.get('id', '')
    data = handle(user_id)
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
