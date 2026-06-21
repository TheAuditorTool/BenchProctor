# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
from flask import request, jsonify


def BenchmarkTest37127():
    upload_name = request.files['upload'].filename
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(upload_name)):
        return jsonify({'error': 'invalid input'}), 400
    processed = upload_name
    return render_template_string(processed)
