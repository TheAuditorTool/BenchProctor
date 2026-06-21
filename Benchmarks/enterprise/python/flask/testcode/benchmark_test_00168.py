# SPDX-License-Identifier: Apache-2.0
import yaml
import os
from flask import jsonify


def BenchmarkTest00168():
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
