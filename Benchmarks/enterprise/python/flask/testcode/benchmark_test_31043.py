# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import re


@dataclass
class FormData:
    payload: str

def BenchmarkTest31043():
    multipart_value = request.form.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})
