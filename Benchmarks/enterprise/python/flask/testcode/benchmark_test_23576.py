# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest23576():
    referer_value = request.headers.get('Referer', '')
    data = handle(referer_value)
    def _primary():
        db.users.find({'$where': "this.username == '" + str(data) + "'"})
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
