# SPDX-License-Identifier: Apache-2.0
import subprocess
import base64
from flask import request, jsonify


def BenchmarkTest14951():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
