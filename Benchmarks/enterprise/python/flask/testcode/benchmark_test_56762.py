# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest56762():
    raw_body = request.get_data(as_text=True)
    if raw_body:
        data = raw_body
    else:
        data = ''
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return jsonify({"result": "success"})
