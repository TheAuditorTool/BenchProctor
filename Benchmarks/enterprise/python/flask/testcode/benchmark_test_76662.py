# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import importlib


@dataclass
class FormData:
    payload: str

def BenchmarkTest76662():
    header_value = request.headers.get('X-Custom-Header', '')
    data = FormData(payload=header_value).payload
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
