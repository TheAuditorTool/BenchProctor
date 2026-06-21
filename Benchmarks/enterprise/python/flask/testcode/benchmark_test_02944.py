# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest02944():
    user_id = request.args.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return jsonify({"result": "success"})
