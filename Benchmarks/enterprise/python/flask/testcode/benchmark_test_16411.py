# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest16411():
    auth_header = request.headers.get('Authorization', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
