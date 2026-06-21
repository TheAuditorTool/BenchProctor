# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest15503():
    field_value = request.form.get('field', '')
    data = ' '.join(str(field_value).split())
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
