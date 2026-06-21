# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
from flask import request, jsonify


def BenchmarkTest76505():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(json_value)):
        return jsonify({'error': 'invalid input'}), 400
    processed = json_value
    return render_template_string(processed)
