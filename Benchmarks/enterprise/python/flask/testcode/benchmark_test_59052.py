# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest59052():
    user_id = request.args.get('id', '')
    data = (lambda v: v.strip())(user_id)
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
