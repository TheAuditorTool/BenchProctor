# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest27293():
    field_value = request.form.get('field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(field_value)
    data = collected
    eval(compile('importlib.import_module(str(data))', '<sink>', 'exec'))
    return jsonify({"result": "success"})
