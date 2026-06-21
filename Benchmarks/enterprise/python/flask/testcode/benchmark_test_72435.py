# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import requests


def BenchmarkTest72435():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
