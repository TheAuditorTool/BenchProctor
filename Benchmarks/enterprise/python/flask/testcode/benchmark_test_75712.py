# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest75712():
    cookie_value = request.cookies.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
