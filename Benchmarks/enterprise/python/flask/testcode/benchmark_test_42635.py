# SPDX-License-Identifier: Apache-2.0
import secrets
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest42635():
    xml_value = request.get_data(as_text=True)
    data = FormData(payload=xml_value).payload
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
