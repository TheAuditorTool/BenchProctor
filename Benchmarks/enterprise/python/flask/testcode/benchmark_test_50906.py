# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify


def BenchmarkTest50906():
    env_value = os.environ.get('USER_INPUT', '')
    requests.post('http://api.prod.internal/data', data=str(env_value))
    return jsonify({"result": "success"})
