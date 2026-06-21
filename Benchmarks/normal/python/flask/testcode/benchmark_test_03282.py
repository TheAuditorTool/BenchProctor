# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import jsonify
import subprocess


@dataclass
class FormData:
    payload: str

def BenchmarkTest03282(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
