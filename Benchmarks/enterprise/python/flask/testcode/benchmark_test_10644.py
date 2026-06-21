# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest10644():
    xml_value = request.get_data(as_text=True)
    data = FormData(payload=xml_value).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return render_template_string(processed)
