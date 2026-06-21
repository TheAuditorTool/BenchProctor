# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest77475():
    field_value = request.form.get('field', '')
    subprocess.Popen('echo ' + str(field_value), shell=True).wait()
    return jsonify({"result": "success"})
