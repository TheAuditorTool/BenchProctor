# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest73409():
    field_value = request.form.get('field', '')
    prefix = ''
    data = prefix + str(field_value)
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
