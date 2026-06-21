# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
import json
from flask import request, jsonify


def BenchmarkTest58304():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
