# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest64153():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
