# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
from flask import redirect
import urllib.parse


def BenchmarkTest13496():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(graphql_var)
    data = collected
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
