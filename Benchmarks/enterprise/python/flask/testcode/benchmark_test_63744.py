# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import json
from flask import request, jsonify


def BenchmarkTest63744():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
