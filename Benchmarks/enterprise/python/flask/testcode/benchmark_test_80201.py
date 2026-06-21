# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest80201():
    cookie_value = request.cookies.get('session_token', '')
    data = default_blank(cookie_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
