# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify


def BenchmarkTest53917():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    requests.get(str(data))
    return jsonify({"result": "success"})
