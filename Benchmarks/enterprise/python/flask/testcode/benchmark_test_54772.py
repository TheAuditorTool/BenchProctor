# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest54772():
    header_value = request.headers.get('X-Custom-Header', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
