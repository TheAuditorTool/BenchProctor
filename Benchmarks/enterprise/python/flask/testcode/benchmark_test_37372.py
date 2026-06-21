# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest37372():
    xml_value = request.get_data(as_text=True)
    data = handle(xml_value)
    json.loads(data)
    return jsonify({"result": "success"})
