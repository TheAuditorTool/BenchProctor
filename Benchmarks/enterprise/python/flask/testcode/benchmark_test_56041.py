# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest56041():
    upload_name = request.files['upload'].filename
    data = '%s' % (upload_name,)
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
