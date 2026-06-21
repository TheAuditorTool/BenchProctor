# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest05265():
    xml_value = request.get_data(as_text=True)
    data = ensure_str(xml_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
