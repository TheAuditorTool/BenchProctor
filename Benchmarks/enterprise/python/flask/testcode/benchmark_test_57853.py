# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify


def BenchmarkTest57853():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
