# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast


def BenchmarkTest11642():
    ua_value = request.headers.get('User-Agent', '')
    try:
        data = str(ast.literal_eval(ua_value))
    except (ValueError, SyntaxError):
        data = ua_value
    eval(compile("with open('/var/app/data/' + str(data), 'w') as fh:\n    fh.write('data')", '<sink>', 'exec'))
    return jsonify({"result": "success"})
