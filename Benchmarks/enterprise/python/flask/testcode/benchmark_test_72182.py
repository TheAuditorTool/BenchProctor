# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
import ast
from app_runtime import db


def BenchmarkTest72182():
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return jsonify({"result": "success"})
