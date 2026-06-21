# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest31664():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % str(header_value)
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
