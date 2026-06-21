# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify


def BenchmarkTest56395():
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
