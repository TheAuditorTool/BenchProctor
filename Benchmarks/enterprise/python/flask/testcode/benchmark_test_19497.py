# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import ast


def BenchmarkTest19497():
    user_id = request.args.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    eval(compile("with open('/var/uploads/' + str(data), 'wb') as fh:\n    fh.write(b'data')", '<sink>', 'exec'))
    return jsonify({"result": "success"})
