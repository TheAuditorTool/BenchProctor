# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest69285():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = handle(dotenv_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
