# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
import sys


def BenchmarkTest13404():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
