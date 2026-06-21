# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify


def BenchmarkTest18797():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
