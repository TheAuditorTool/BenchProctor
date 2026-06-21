# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest06291(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
