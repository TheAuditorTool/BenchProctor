# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest75593():
    field_value = request.form.get('field', '')
    parts = []
    for token in str(field_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
