# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request, jsonify


def BenchmarkTest72347():
    xml_value = request.get_data(as_text=True)
    if xml_value not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = xml_value
    return render_template_string(processed)
