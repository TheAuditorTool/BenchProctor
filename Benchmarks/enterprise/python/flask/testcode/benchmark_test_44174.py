# SPDX-License-Identifier: Apache-2.0
import logging
import os
from flask import jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest44174():
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
