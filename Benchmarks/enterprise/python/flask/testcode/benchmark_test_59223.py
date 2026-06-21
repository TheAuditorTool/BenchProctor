# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify


def BenchmarkTest59223():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
