# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest63194():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
