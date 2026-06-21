# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest13664():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
