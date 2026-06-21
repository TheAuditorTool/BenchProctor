# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
import sys


def BenchmarkTest12532():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    sys.path.insert(0, str(forwarded_ip))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
