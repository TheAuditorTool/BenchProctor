# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import importlib


def relay_value(value):
    return value

def BenchmarkTest06376():
    field_value = request.form.get('field', '')
    data = relay_value(field_value)
    if os.environ.get("APP_ENV", "production") != "test":
        importlib.import_module(str(data))
    return jsonify({"result": "success"})
