# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest33674():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
