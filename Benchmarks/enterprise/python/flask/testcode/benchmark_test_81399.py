# SPDX-License-Identifier: Apache-2.0
import threading
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest81399():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
