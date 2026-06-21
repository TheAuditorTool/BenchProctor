# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest30843():
    field_value = request.form.get('field', '')
    data = (lambda v: v.strip())(field_value)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
