# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import redirect
import urllib.parse


def BenchmarkTest53654():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    prefix = ''
    data = prefix + str(graphql_var)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
