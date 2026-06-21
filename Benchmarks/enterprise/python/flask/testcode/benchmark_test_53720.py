# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import jsonify
import importlib
import sys


def BenchmarkTest53720(path_param):
    path_value = path_param
    data = unquote(path_value)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
