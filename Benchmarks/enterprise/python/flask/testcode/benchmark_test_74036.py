# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest74036(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    eval(str(data))
    return jsonify({"result": "success"})
