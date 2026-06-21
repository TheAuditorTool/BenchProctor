# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify


def BenchmarkTest46332():
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
