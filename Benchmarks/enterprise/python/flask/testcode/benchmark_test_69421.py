# SPDX-License-Identifier: Apache-2.0
import os
import re
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest69421():
    field_value = request.form.get('field', '')
    data = FormData(payload=field_value).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
