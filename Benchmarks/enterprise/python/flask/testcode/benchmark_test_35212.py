# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest35212():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % (auth_header,)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return jsonify({"result": "success"})
