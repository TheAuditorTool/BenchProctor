# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest53772():
    raw_body = request.get_data(as_text=True)
    subprocess.run('echo ' + str(raw_body), shell=True)
    return jsonify({"result": "success"})
