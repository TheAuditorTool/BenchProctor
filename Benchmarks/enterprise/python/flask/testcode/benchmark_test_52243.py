# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import subprocess


def BenchmarkTest52243(path_param):
    path_value = path_param
    kind = 'json' if str(path_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = path_value
            data = parsed
        case _:
            data = path_value
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
