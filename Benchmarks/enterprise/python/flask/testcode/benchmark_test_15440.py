# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import requests
from flask import jsonify
import time


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest15440():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = handle(api_value)
    if time.time() > 1000000000:
        return redirect(str(data))
    return jsonify({"result": "success"})
