# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest73784():
    ua_value = request.headers.get('User-Agent', '')
    ctx = RequestContext(ua_value)
    data = ctx.payload
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
