# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify


def BenchmarkTest01520():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    requests.get(str(data))
    return jsonify({"result": "success"})
