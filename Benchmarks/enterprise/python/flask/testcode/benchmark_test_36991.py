# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest36991():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    ctx = RequestContext(prop_value)
    data = ctx.payload
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
