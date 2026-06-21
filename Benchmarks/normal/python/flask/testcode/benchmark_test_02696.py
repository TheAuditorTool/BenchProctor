# SPDX-License-Identifier: Apache-2.0
import yaml
import os
from flask import jsonify


def BenchmarkTest02696():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    yaml.safe_load(data)
    return jsonify({"result": "success"})
