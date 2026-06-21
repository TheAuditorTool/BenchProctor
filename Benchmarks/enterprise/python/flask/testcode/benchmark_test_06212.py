# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest06212(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
