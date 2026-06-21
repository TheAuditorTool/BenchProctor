# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import requests


@dataclass
class FormData:
    payload: str

def BenchmarkTest72327():
    user_id = request.args.get('id', '')
    data = FormData(payload=user_id).payload
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
