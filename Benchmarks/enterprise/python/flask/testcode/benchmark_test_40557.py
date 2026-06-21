# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest40557():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    ctx = RequestContext(config_value)
    data = ctx.payload
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
