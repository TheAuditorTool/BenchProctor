# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify
import ast


def BenchmarkTest09778():
    xml_value = request.get_data(as_text=True)
    try:
        data = str(ast.literal_eval(xml_value))
    except (ValueError, SyntaxError):
        data = xml_value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
