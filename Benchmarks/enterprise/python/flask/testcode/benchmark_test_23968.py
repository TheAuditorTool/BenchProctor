# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import jsonify


def BenchmarkTest23968(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
