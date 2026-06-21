# SPDX-License-Identifier: Apache-2.0
import subprocess
import shlex
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest62106():
    stdin_value = input('input: ')
    ctx = RequestContext(stdin_value)
    data = ctx.payload
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
