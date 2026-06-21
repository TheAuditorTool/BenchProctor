# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest76855():
    header_value = request.headers.get('X-Custom-Header', '')
    data = bytes.fromhex(header_value).decode('utf-8', 'ignore')
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
