# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import jsonify


def BenchmarkTest08993(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return jsonify({"result": "success"})
