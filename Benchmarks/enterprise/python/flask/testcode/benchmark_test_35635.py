# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest35635():
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    requests.get(str(data))
    return jsonify({"result": "success"})
