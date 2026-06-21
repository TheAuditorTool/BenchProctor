# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest13245():
    stdin_value = input('input: ')
    ctx = RequestContext(stdin_value)
    data = ctx.payload
    eval(compile("subprocess.Popen('echo ' + str(data), shell=True).wait()", '<sink>', 'exec'))
    return jsonify({"result": "success"})
