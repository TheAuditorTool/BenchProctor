# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest15068():
    upload_name = request.files['upload'].filename
    data = '{}'.format(upload_name)
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
