# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast


def BenchmarkTest36352():
    multipart_value = request.form.get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
