# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify


def BenchmarkTest09183():
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
