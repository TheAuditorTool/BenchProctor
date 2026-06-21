# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest50960():
    origin_value = request.headers.get('Origin', '')
    data = ' '.join(str(origin_value).split())
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
