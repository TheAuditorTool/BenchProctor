# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest11602():
    user_id = request.args.get('id', '')
    data = '%s' % str(user_id)
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
