# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import importlib


def to_text(value):
    return str(value).strip()

def BenchmarkTest53540():
    field_value = request.form.get('field', '')
    data = to_text(field_value)
    if os.environ.get("APP_ENV", "production") != "test":
        importlib.import_module(str(data))
    return jsonify({"result": "success"})
