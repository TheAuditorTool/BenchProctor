# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import jsonify


def BenchmarkTest03872(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
