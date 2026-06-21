# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest50079():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
