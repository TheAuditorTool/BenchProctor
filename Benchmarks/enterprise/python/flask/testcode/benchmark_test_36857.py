# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest36857():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    parts = str(json_value).split(',')
    data = ','.join(parts)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return jsonify({"result": "success"})
