# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
from flask import request, jsonify


def BenchmarkTest33787():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
