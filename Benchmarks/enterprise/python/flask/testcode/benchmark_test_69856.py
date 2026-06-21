# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request, jsonify


def BenchmarkTest69856():
    auth_header = request.headers.get('Authorization', '')
    data = str(auth_header).replace('\x00', '')
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
