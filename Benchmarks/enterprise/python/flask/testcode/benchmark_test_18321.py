# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import runpy


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest18321():
    auth_header = request.headers.get('Authorization', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    eval(compile('with open(\'plugins/generated_config.py\', \'w\') as fh:\n    fh.write(\'SETTING = "\' + str(data) + \'"\')\nrunpy.run_path(\'plugins/generated_config.py\')', '<sink>', 'exec'))
    return jsonify({"result": "success"})
