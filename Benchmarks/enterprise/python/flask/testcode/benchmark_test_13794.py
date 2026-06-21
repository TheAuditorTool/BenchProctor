# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import urllib.request


def BenchmarkTest13794():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
