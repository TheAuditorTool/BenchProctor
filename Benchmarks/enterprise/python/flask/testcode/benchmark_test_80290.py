# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import subprocess


def BenchmarkTest80290(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
