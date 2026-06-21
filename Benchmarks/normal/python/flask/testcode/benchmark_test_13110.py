# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest13110():
    referer_value = request.headers.get('Referer', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
