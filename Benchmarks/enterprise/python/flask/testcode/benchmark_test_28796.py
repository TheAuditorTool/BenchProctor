# SPDX-License-Identifier: Apache-2.0
import logging
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest28796():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
