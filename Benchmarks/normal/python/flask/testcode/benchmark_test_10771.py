# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
from flask import request, jsonify


def BenchmarkTest10771():
    origin_value = request.headers.get('Origin', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(origin_value)):
        return jsonify({'error': 'invalid input'}), 400
    processed = origin_value
    return Markup('<div>' + str(processed) + '</div>')
