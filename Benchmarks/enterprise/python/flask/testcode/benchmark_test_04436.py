# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import importlib


def BenchmarkTest04436():
    env_value = os.environ.get('USER_INPUT', '')
    importlib.import_module(str(env_value))
    return jsonify({"result": "success"})
