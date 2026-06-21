# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import importlib


@dataclass
class FormData:
    payload: str

def BenchmarkTest29539():
    multipart_value = request.form.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
