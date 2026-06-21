# SPDX-License-Identifier: Apache-2.0
import subprocess
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest12845():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
