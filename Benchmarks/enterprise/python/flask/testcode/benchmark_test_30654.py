# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request, jsonify


def BenchmarkTest30654():
    cookie_value = request.cookies.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
