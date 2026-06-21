# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import jsonify


def BenchmarkTest30479(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
