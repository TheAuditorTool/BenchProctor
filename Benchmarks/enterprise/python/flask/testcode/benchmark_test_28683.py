# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest28683():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
