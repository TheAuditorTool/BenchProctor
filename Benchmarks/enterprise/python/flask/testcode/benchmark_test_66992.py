# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import urllib.request


def BenchmarkTest66992():
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
