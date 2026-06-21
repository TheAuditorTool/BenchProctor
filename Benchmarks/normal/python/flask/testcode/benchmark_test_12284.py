# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest12284():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
