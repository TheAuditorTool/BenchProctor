# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
import ast


def BenchmarkTest23148():
    ua_value = request.headers.get('User-Agent', '')
    try:
        data = str(ast.literal_eval(ua_value))
    except (ValueError, SyntaxError):
        data = ua_value
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
