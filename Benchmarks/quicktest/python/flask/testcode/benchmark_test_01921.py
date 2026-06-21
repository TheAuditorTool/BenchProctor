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

def BenchmarkTest01921():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = handle(forwarded_ip)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
