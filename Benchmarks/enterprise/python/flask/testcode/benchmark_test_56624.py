# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest56624():
    origin_value = request.headers.get('Origin', '')
    data = (lambda v: v.strip())(origin_value)
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
