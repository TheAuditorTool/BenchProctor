# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest32310():
    auth_header = request.headers.get('Authorization', '')
    data = FormData(payload=auth_header).payload
    os.remove(str(data))
    return jsonify({"result": "success"})
