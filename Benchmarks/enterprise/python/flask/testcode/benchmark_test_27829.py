# SPDX-License-Identifier: Apache-2.0
import yaml
import json
import os
from flask import jsonify


def BenchmarkTest27829():
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    yaml.safe_load(data)
    return jsonify({"result": "success"})
