# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest64338():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json_value if json_value else 'default'
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return jsonify({"result": "success"})
