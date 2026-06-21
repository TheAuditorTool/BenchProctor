# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest35428():
    xml_value = request.get_data(as_text=True)
    data = FormData(payload=xml_value).payload
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
