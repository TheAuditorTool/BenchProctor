# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest75415():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
