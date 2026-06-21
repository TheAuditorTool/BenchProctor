# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest66630():
    field_value = request.form.get('field', '')
    data = (lambda v: v.strip())(field_value)
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
