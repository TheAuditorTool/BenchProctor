# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
import importlib


def BenchmarkTest02153():
    field_value = request.form.get('field', '')
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
