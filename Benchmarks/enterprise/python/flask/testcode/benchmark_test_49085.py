# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest49085():
    header_value = request.headers.get('X-Custom-Header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return jsonify({"result": "success"})
