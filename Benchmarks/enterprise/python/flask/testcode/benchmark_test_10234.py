# SPDX-License-Identifier: Apache-2.0
import subprocess
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest10234(path_param):
    path_value = path_param
    data = unquote(path_value)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return jsonify({"result": "success"})
