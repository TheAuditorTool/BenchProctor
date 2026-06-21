# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import importlib


@dataclass
class FormData:
    payload: str

def BenchmarkTest23373():
    field_value = request.form.get('field', '')
    data = FormData(payload=field_value).payload
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
