# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import json
import subprocess


def BenchmarkTest28786():
    multipart_value = request.form.get('multipart_field', '')
    try:
        data = json.loads(multipart_value).get('value', multipart_value)
    except (json.JSONDecodeError, AttributeError):
        data = multipart_value
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
