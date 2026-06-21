# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
from flask import request, jsonify


def BenchmarkTest11147():
    upload_name = request.files['upload'].filename
    data, _sep, _rest = str(upload_name).partition('\x00')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return render_template_string(processed)
