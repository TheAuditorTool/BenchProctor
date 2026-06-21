# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
import importlib


def BenchmarkTest15905():
    referer_value = request.headers.get('Referer', '')
    try:
        data = json.loads(referer_value).get('value', referer_value)
    except (json.JSONDecodeError, AttributeError):
        data = referer_value
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
