# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest26006():
    origin_value = request.headers.get('Origin', '')
    data = FormData(payload=origin_value).payload
    requests.get(str(data))
    return jsonify({"result": "success"})
