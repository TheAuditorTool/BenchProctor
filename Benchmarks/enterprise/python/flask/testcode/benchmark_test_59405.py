# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest59405():
    cookie_value = request.cookies.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
