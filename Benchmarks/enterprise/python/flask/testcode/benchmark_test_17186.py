# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest17186():
    upload_name = request.files['upload'].filename
    ctx = RequestContext(upload_name)
    data = ctx.payload
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
