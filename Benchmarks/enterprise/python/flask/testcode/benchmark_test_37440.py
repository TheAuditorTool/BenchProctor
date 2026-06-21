# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
import sys


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest37440():
    multipart_value = request.form.get('multipart_field', '')
    data = handle(multipart_value)
    eval(compile("sys.path.insert(0, str(data))\nimportlib.import_module('report_renderer')", '<sink>', 'exec'))
    return jsonify({"result": "success"})
