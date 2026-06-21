# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest31616():
    origin_value = request.headers.get('Origin', '')
    data = FormData(payload=origin_value).payload
    os.remove(str(data))
    return jsonify({"result": "success"})
