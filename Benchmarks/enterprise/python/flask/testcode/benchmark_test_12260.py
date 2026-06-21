# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest12260():
    referer_value = request.headers.get('Referer', '')
    data = to_text(referer_value)
    if not re.fullmatch('^[\\w\\s<>\\"\'/().;=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
