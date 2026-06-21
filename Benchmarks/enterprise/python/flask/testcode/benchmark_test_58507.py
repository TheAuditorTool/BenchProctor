# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import importlib
import sys


def BenchmarkTest58507():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
