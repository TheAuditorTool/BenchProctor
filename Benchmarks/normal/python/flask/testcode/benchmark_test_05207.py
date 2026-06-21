# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest05207():
    field_value = request.form.get('field', '')
    data = FormData(payload=field_value).payload
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
