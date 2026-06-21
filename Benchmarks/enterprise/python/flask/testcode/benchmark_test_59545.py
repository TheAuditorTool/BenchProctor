# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest59545():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return render_template_string(processed)
