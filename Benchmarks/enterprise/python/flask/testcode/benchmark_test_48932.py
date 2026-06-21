# SPDX-License-Identifier: Apache-2.0
import yaml
import os
from flask import jsonify


def BenchmarkTest48932():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
