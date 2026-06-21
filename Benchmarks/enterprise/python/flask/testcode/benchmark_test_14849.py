# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import importlib
import sys


def BenchmarkTest14849(path_param):
    path_value = path_param
    sys.path.insert(0, str(path_value))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
