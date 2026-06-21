# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
import os
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest68124():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
