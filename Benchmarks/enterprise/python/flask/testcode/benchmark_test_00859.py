# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest00859():
    field_value = request.form.get('field', '')
    data = (lambda v: v.strip())(field_value)
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
