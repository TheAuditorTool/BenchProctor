# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
from flask import request, jsonify


def BenchmarkTest47141():
    raw_body = request.get_data(as_text=True)
    data, _sep, _rest = str(raw_body).partition('\x00')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<img src="' + str(processed) + '">')
