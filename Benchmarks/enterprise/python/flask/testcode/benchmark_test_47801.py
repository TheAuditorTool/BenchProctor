# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import requests


def BenchmarkTest47801():
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
