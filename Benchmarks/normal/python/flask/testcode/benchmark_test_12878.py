# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest12878():
    upload_name = request.files['upload'].filename
    data = to_text(upload_name)
    processed = data[:64]
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
