# SPDX-License-Identifier: Apache-2.0
import threading
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest68458():
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
