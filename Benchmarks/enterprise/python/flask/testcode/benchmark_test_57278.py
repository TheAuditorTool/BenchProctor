# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
import sys


def BenchmarkTest57278():
    referer_value = request.headers.get('Referer', '')
    sys.path.insert(0, str(referer_value))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
