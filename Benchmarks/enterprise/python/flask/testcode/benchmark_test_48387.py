# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def BenchmarkTest48387():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
