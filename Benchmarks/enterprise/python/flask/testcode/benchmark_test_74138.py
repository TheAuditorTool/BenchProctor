# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest74138():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return jsonify({"result": "success"})
