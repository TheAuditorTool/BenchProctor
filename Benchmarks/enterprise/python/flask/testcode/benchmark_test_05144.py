# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest05144(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    eval(compile("subprocess.run('echo ' + str(data), shell=True)", '<sink>', 'exec'))
    return jsonify({"result": "success"})
