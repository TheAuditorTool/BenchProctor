# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import requests


@dataclass
class FormData:
    payload: str

def BenchmarkTest30614():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
