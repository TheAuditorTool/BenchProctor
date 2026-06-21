# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest11469():
    upload_name = request.files['upload'].filename
    data = ensure_str(upload_name)
    if not re.fullmatch('^[\\w\\s<>\\"\'/().;=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
