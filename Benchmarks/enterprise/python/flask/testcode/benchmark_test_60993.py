# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import jsonify


def BenchmarkTest60993(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
