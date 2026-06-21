# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest69686():
    field_value = request.form.get('field', '')
    data = handle(field_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
