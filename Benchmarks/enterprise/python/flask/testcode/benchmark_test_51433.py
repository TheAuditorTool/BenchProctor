# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest51433():
    referer_value = request.headers.get('Referer', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
