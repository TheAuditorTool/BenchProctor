# SPDX-License-Identifier: Apache-2.0
import subprocess
import shlex
from flask import request, jsonify


def BenchmarkTest08620():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    if json_value:
        data = json_value
    else:
        data = ''
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
