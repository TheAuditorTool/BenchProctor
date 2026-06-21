# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
import sys


def BenchmarkTest49395():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
