# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest15697():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
