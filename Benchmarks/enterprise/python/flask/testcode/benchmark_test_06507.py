# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify


def BenchmarkTest06507():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
