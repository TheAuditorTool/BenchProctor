# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import time
import ast


def BenchmarkTest19045():
    multipart_value = request.form.get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return jsonify({"result": "success"})
