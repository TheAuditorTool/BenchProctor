# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import importlib
import sys


def BenchmarkTest75659(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
