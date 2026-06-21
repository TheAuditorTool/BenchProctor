# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast
import importlib
import sys


def BenchmarkTest57655():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    try:
        data = str(ast.literal_eval(forwarded_ip))
    except (ValueError, SyntaxError):
        data = forwarded_ip
    eval(compile("sys.path.insert(0, str(data))\nimportlib.import_module('report_renderer')", '<sink>', 'exec'))
    return jsonify({"result": "success"})
