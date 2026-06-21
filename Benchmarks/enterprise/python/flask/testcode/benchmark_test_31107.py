# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
import sys


def BenchmarkTest31107():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
