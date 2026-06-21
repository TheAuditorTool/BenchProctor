# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest40235():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    ctx = RequestContext(query_array)
    data = ctx.payload
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
