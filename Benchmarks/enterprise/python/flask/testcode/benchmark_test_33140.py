# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest33140():
    upload_name = request.files['upload'].filename
    data = handle(upload_name)
    def _primary():
        _resp = requests.get(str(data))
        exec(_resp.text)
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
