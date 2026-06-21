# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest03437():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
