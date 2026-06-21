# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import os
from flask import jsonify
import requests


@dataclass
class FormData:
    payload: str

def BenchmarkTest16386():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
