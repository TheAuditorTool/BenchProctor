# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify
import time


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest15207():
    xml_value = request.get_data(as_text=True)
    data = handle(xml_value)
    if time.time() > 1000000000:
        yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
