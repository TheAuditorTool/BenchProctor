# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
import sys


def BenchmarkTest14402():
    origin_value = request.headers.get('Origin', '')
    sys.path.insert(0, str(origin_value))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
