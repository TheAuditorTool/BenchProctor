# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import time
import subprocess


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest51895():
    host_value = request.headers.get('Host', '')
    data = handle(host_value)
    if time.time() > 1000000000:
        subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
