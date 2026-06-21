# SPDX-License-Identifier: Apache-2.0
import subprocess
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest00316():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
