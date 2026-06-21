# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import ast


def BenchmarkTest09998():
    user_id = request.args.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    processed = data[:64]
    with open('/var/uploads/' + str(processed), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
