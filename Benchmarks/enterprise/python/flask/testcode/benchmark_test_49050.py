# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest49050():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '{}'.format(header_value)
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
