# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request, jsonify


def BenchmarkTest25060():
    cookie_value = request.cookies.get('session_token', '')
    if cookie_value not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = cookie_value
    return render_template_string(processed)
