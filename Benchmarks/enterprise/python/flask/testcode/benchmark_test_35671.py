# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
import os
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest35671():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
