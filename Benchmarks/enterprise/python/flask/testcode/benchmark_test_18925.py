# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest18925():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = coalesce_blank(json_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<img src="' + str(processed) + '">')
