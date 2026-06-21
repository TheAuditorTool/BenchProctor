# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest20086():
    xml_value = request.get_data(as_text=True)
    data = (lambda v: v.strip())(xml_value)
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
