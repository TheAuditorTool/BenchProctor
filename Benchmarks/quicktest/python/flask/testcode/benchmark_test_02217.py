# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import importlib


@dataclass
class FormData:
    payload: str

def BenchmarkTest02217():
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
