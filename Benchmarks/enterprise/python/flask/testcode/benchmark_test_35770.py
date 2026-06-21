# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
import importlib


def BenchmarkTest35770():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
