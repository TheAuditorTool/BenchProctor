# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
from flask import request, jsonify


def BenchmarkTest33537():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return render_template_string(processed)
