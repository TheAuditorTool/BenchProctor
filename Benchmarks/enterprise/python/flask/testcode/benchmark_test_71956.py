# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify


def BenchmarkTest71956():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
