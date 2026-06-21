# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest06811(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
