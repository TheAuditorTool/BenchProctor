# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request, jsonify


def BenchmarkTest04239():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
