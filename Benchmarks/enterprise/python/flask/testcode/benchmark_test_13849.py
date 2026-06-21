# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest13849():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
