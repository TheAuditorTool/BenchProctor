# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
import ast
from app_runtime import db


def BenchmarkTest31526():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return jsonify({"result": "success"})
