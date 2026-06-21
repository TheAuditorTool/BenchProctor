# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import jsonify


def BenchmarkTest72068(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
