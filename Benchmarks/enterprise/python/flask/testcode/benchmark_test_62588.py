# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify
import ast


def BenchmarkTest62588():
    upload_name = request.files['upload'].filename
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
