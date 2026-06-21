# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest11016():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
