# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest73658():
    user_id = request.args.get('id', '')
    data = handle(user_id)
    def _primary():
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
