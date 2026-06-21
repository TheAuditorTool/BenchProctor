# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify


def BenchmarkTest50730():
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    requests.get(str(data))
    return jsonify({"result": "success"})
