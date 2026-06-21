# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request, jsonify


def BenchmarkTest12145():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
