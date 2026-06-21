# SPDX-License-Identifier: Apache-2.0
import yaml
import json
import os
from flask import jsonify


def BenchmarkTest38611():
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    yaml.safe_load(data)
    return jsonify({"result": "success"})
