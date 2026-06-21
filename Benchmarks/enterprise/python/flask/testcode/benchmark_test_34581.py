# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest34581():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
