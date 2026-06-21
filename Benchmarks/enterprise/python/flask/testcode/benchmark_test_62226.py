# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
import ast


def BenchmarkTest62226():
    origin_value = request.headers.get('Origin', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
