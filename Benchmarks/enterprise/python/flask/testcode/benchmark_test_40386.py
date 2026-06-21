# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest40386():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
