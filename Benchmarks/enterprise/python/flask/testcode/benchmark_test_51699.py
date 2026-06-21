# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest51699():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
