# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import auth_check


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest80708():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    ctx = RequestContext(yaml_value)
    data = ctx.payload
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
