# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest51445():
    upload_name = request.files['upload'].filename
    data = FormData(payload=upload_name).payload
    return jsonify({'error': 'An internal error occurred'}), 500
