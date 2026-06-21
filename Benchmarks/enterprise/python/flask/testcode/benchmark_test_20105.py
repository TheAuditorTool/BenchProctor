# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
from flask import jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest20105(path_param):
    path_value = path_param
    data = default_blank(path_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
