# SPDX-License-Identifier: Apache-2.0
import subprocess
import shlex
from flask import request, jsonify


def BenchmarkTest02485():
    referer_value = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
