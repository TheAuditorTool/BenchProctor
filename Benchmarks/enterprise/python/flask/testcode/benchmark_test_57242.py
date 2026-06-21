# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest57242():
    multipart_value = request.form.get('multipart_field', '')
    subprocess.run([str(multipart_value), '--status'], shell=False)
    return jsonify({"result": "success"})
