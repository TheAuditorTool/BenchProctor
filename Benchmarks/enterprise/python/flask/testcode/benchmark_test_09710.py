# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import json


def BenchmarkTest09710():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    json.loads(data)
    return jsonify({"result": "success"})
