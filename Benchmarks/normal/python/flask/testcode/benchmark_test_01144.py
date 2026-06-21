# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify


def BenchmarkTest01144():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
