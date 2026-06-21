# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
import sys


def BenchmarkTest08584():
    auth_header = request.headers.get('Authorization', '')
    sys.path.insert(0, str(auth_header))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
