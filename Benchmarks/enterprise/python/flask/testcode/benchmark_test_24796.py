# SPDX-License-Identifier: Apache-2.0
import subprocess
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest24796(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
