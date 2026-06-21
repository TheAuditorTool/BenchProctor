# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import importlib
import sys


def BenchmarkTest46018():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
