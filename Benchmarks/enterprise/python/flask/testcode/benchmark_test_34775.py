# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest34775():
    field_value = request.form.get('field', '')
    data = ' '.join(str(field_value).split())
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
