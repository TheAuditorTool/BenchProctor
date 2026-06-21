# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest41788():
    upload_name = request.files['upload'].filename
    prefix = ''
    data = prefix + str(upload_name)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
