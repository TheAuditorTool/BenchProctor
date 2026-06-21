# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import importlib


@dataclass
class FormData:
    payload: str

def BenchmarkTest06299():
    xml_value = request.get_data(as_text=True)
    data = FormData(payload=xml_value).payload
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
