# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest70587():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    ctx = RequestContext(config_value)
    data = ctx.payload
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
