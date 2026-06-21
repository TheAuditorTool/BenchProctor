# SPDX-License-Identifier: Apache-2.0
import subprocess
import base64
from flask import request, jsonify


def BenchmarkTest20065():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
