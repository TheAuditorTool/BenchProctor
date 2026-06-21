# SPDX-License-Identifier: Apache-2.0
import os
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

def BenchmarkTest21851():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = handle(api_value)
    if time.time() > 1000000000:
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    return jsonify({"result": "success"})
