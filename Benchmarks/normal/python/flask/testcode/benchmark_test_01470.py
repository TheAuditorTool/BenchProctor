# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest01470():
    referer_value = request.headers.get('Referer', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
