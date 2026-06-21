# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import importlib
import sys


def BenchmarkTest43268(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
