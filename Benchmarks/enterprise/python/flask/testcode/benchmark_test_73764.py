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

def BenchmarkTest73764():
    upload_name = request.files['upload'].filename
    data = handle(upload_name)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
