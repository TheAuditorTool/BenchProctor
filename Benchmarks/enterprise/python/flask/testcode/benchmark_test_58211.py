# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest58211():
    host_value = request.headers.get('Host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
