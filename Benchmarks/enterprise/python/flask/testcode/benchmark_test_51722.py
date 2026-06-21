# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import importlib
import sys


def BenchmarkTest51722():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
