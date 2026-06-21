# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def to_text(value):
    return str(value).strip()

def BenchmarkTest23432():
    header_value = request.headers.get('X-Custom-Header', '')
    data = to_text(header_value)
    eval(compile('importlib.import_module(str(data))', '<sink>', 'exec'))
    return jsonify({"result": "success"})
