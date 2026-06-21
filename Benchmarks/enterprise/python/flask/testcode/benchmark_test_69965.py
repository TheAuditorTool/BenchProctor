# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import importlib
import sys


def BenchmarkTest69965(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
