# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest19812():
    upload_name = request.files['upload'].filename
    data = normalise_input(upload_name)
    if not re.fullmatch('^[\\w\\s<>\\"\'/().;=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
