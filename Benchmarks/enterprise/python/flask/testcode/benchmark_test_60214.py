# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import json


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest60214():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = handle(api_value)
    json.loads(data)
    return jsonify({"result": "success"})
