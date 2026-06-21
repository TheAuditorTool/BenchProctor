# SPDX-License-Identifier: Apache-2.0
import subprocess
import json
from flask import request, jsonify


def BenchmarkTest37735():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
