# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest05050(path_param):
    path_value = path_param
    data = handle(path_value)
    checked_path = os.path.normpath(data)
    os.unlink('/var/app/data/' + str(checked_path))
    return jsonify({"result": "success"})
