# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
import sys


def BenchmarkTest12299():
    ua_value = request.headers.get('User-Agent', '')
    sys.path.insert(0, str(ua_value))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
