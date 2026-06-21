# SPDX-License-Identifier: Apache-2.0
import os
from urllib.parse import unquote
from flask import request, jsonify
import subprocess


def BenchmarkTest51400():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
