# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest32126():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value}'
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
