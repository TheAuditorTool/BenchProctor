# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import importlib
import sys


def BenchmarkTest46651():
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
