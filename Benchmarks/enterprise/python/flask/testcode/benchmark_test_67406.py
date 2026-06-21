# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest67406():
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    os.remove(str(data))
    return jsonify({"result": "success"})
