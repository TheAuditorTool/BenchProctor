# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
import sys


def BenchmarkTest61424():
    host_value = request.headers.get('Host', '')
    sys.path.insert(0, str(host_value))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
