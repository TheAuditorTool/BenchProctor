# SPDX-License-Identifier: Apache-2.0
import logging
import os
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest29821():
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
