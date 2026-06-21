# SPDX-License-Identifier: Apache-2.0
import subprocess
import shlex
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest14440():
    auth_header = request.headers.get('Authorization', '')
    data = relay_value(auth_header)
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
