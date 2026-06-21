# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def BenchmarkTest34495():
    field_value = request.form.get('field', '')
    prefix = ''
    data = prefix + str(field_value)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
