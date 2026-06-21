# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest25061():
    field_value = request.form.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
