# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest50670():
    referer_value = request.headers.get('Referer', '')
    data = normalise_input(referer_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
