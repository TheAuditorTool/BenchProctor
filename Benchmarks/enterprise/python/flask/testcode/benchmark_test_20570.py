# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest20570():
    field_value = request.form.get('field', '')
    data = f'{field_value}'
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return jsonify({"result": "success"})
