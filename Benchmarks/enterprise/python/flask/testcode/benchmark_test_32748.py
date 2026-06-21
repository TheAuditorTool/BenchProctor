# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import defusedxml.ElementTree


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest32748(path_param):
    path_value = path_param
    data = handle(path_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
