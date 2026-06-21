# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest54864():
    cookie_value = request.cookies.get('session_token', '')
    data = normalise_input(cookie_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
