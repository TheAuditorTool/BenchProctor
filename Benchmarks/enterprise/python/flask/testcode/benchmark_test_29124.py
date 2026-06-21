# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
import ast


def BenchmarkTest29124():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    try:
        data = str(ast.literal_eval(query_array))
    except (ValueError, SyntaxError):
        data = query_array
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
