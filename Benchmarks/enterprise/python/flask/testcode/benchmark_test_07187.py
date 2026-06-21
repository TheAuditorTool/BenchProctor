# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
from flask import request, jsonify


def BenchmarkTest07187():
    multipart_value = request.form.get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
