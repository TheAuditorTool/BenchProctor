# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
import requests


@dataclass
class FormData:
    payload: str

def BenchmarkTest02896(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
