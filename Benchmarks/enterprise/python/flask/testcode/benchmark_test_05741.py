# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import requests


@dataclass
class FormData:
    payload: str

def BenchmarkTest05741():
    host_value = request.headers.get('Host', '')
    data = FormData(payload=host_value).payload
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
