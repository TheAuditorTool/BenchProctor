# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest11725():
    raw_body = request.get_data(as_text=True)
    data = ' '.join(str(raw_body).split())
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
