# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
from flask import request, jsonify


def BenchmarkTest67334():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', json_value):
        return jsonify({'error': 'forbidden'}), 400
    processed = json_value
    return Markup('<div>' + str(processed) + '</div>')
