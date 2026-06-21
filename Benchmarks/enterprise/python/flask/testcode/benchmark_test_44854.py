# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest44854(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    os.remove(str(data))
    return jsonify({"result": "success"})
