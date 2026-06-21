# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest17742(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
