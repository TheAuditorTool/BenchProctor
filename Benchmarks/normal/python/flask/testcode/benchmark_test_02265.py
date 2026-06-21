# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest02265():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value}'
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return jsonify({"result": "success"})
