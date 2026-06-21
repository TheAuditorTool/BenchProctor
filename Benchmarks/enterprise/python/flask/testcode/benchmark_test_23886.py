# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request, jsonify


def BenchmarkTest23886():
    ua_value = request.headers.get('User-Agent', '')
    if ua_value not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = ua_value
    return render_template_string(processed)
