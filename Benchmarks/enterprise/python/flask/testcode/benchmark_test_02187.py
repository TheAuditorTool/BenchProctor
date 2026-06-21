# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest02187():
    env_value = os.environ.get('USER_INPUT', '')
    data = ensure_str(env_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
