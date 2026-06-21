# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest00306():
    field_value = request.form.get('field', '')
    importlib.import_module(str(field_value))
    return jsonify({"result": "success"})
