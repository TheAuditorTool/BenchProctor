# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def BenchmarkTest61292():
    field_value = request.form.get('field', '')
    subprocess.run(['echo', field_value], shell=False)
    return jsonify({"result": "success"})
