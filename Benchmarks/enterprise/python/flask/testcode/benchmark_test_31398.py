# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify


def BenchmarkTest31398():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    requests.get(str(data))
    return jsonify({"result": "success"})
