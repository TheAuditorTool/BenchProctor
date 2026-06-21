# SPDX-License-Identifier: Apache-2.0
import subprocess
import shlex
from flask import request, jsonify


def BenchmarkTest63165():
    header_value = request.headers.get('X-Custom-Header', '')
    data = str(header_value).replace('\x00', '')
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
