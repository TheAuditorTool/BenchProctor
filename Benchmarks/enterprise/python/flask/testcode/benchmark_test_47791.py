# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import jsonify


def BenchmarkTest47791(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
