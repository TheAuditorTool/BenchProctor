# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import base64
from flask import request, jsonify


def BenchmarkTest04140():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
