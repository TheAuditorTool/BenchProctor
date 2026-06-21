# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest41829():
    xml_value = request.get_data(as_text=True)
    data = handle(xml_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
