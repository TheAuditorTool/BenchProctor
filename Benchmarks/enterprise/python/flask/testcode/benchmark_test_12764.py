# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest12764(path_param):
    path_value = path_param
    data = handle(path_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
