# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest26311():
    xml_value = request.get_data(as_text=True)
    data = handle(xml_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
