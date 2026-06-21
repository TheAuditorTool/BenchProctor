# SPDX-License-Identifier: Apache-2.0
import yaml
import os
from flask import jsonify


def BenchmarkTest37459():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
