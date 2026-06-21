# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest40169():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    request_state['last_input'] = query_array
    data = request_state['last_input']
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
