# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import requests


def BenchmarkTest11445():
    env_value = os.environ.get('USER_INPUT', '')
    prefix = ''
    data = prefix + str(env_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
