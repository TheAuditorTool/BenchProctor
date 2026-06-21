# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import jsonify


def BenchmarkTest10885(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
