# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest01904():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
