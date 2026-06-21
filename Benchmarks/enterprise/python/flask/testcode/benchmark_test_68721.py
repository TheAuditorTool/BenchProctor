# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest68721(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
