# SPDX-License-Identifier: Apache-2.0
import subprocess
import base64
from flask import request, jsonify


def BenchmarkTest40652():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return jsonify({"result": "success"})
