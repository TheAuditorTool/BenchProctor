# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import jsonify


def BenchmarkTest66024(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
