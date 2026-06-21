# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest32444():
    host_value = request.headers.get('Host', '')
    data = FormData(payload=host_value).payload
    os.remove(str(data))
    return jsonify({"result": "success"})
