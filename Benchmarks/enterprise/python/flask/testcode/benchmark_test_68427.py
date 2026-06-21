# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest68427():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
