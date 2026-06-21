# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import importlib


def BenchmarkTest01457():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
