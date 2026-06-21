# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest58008():
    origin_value = request.headers.get('Origin', '')
    importlib.import_module(str(origin_value))
    return jsonify({"result": "success"})
