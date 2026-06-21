# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest42412():
    upload_name = request.files['upload'].filename
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
