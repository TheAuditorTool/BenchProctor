# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest06234():
    auth_header = request.headers.get('Authorization', '')
    data = handle(auth_header)
    def _primary():
        subprocess.Popen('echo ' + str(data), shell=True).wait()
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
