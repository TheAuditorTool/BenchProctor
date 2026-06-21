# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest61014():
    xml_value = request.get_data(as_text=True)
    data = FormData(payload=xml_value).payload
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
