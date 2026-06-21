# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest04136():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    ctx = RequestContext(query_array)
    data = ctx.payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
