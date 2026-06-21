# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast
import defusedxml.ElementTree


def BenchmarkTest47017():
    host_value = request.headers.get('Host', '')
    try:
        data = str(ast.literal_eval(host_value))
    except (ValueError, SyntaxError):
        data = host_value
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
