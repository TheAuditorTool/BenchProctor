# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest35211():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % (auth_header,)
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
