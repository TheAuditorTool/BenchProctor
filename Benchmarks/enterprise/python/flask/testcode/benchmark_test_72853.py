# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest72853():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value}'
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
