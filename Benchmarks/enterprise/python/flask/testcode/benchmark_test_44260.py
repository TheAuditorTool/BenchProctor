# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest44260():
    host_value = request.headers.get('Host', '')
    data = f'{host_value}'
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
