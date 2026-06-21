# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import importlib


def BenchmarkTest67684():
    env_value = os.environ.get('USER_INPUT', '')
    prefix = ''
    data = prefix + str(env_value)
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
