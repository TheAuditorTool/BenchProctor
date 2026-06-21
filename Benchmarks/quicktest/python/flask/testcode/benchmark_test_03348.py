# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import re


@dataclass
class FormData:
    payload: str

def BenchmarkTest03348():
    raw_body = request.get_data(as_text=True)
    data = FormData(payload=raw_body).payload
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})
