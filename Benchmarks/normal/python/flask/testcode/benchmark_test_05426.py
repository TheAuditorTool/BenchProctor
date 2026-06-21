# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast


def BenchmarkTest05426():
    referer_value = request.headers.get('Referer', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    processed = data[:64]
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(processed))
    return jsonify({"result": "success"})
