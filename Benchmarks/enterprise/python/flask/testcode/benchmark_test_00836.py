# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest00836(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
