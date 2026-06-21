# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest66117(path_param):
    path_value = path_param
    data = unquote(path_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
