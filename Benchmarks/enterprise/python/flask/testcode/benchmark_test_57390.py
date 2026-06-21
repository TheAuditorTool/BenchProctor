# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest57390():
    upload_name = request.files['upload'].filename
    data = normalise_input(upload_name)
    processed = data[:64]
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
