# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import requests
from flask import jsonify
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest07555():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = handle(api_value)
    if os.environ.get("APP_ENV", "production") != "test":
        return redirect(str(data))
    return jsonify({"result": "success"})
