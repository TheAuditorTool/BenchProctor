# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
import importlib


def BenchmarkTest05412():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
