# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest08375():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = default_blank(graphql_var)
    if not re.fullmatch('^[\\w\\s<>\\"\'/(){}.*]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
