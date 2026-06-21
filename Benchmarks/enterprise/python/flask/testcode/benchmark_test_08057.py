# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest08057(path_param):
    path_value = path_param
    data = handle(path_value)
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
