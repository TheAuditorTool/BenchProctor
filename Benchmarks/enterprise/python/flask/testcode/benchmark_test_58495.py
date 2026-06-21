# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest58495():
    xml_value = request.get_data(as_text=True)
    ctx = RequestContext(xml_value)
    data = ctx.payload
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
