# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import importlib


def BenchmarkTest45647():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
