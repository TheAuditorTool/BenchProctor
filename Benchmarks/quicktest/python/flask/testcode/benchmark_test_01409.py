# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest01409():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value:.200s}'
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
