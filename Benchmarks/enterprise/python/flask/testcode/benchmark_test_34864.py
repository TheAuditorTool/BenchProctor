# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest34864():
    header_value = request.headers.get('X-Custom-Header', '')
    data = FormData(payload=header_value).payload
    os.remove(str(data))
    return jsonify({"result": "success"})
