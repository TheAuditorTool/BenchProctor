# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request, jsonify


def BenchmarkTest14280():
    referer_value = request.headers.get('Referer', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
