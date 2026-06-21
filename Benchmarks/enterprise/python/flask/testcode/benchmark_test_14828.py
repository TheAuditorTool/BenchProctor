# SPDX-License-Identifier: Apache-2.0
import subprocess
import shlex
from flask import jsonify


def BenchmarkTest14828(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
