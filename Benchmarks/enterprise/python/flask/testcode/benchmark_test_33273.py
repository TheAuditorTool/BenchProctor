# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import jsonify


def BenchmarkTest33273(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return jsonify({"result": "success"})
