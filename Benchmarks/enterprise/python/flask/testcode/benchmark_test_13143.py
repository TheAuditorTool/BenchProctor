# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest13143():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = ' '.join(str(json_value).split())
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return jsonify({"result": "success"})
