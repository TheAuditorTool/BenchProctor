# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest02873():
    field_value = request.form.get('field', '')
    data = default_blank(field_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
