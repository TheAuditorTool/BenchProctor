# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest39074():
    raw_body = request.get_data(as_text=True)
    subprocess.Popen('echo ' + str(raw_body), shell=True).wait()
    return jsonify({"result": "success"})
