# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest67918():
    auth_header = request.headers.get('Authorization', '')
    data = relay_value(auth_header)
    processed = data[:64]
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return jsonify({"result": "success"})
