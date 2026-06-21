# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest02693():
    field_value = request.form.get('field', '')
    data = '%s' % str(field_value)
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
