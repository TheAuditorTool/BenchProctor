# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest75854():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
