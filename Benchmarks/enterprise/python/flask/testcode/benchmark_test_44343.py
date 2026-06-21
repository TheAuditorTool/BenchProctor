# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest44343(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<img src="' + str(processed) + '">')
