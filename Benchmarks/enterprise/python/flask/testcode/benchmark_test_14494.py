# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
from flask import request, jsonify


def BenchmarkTest14494():
    upload_name = request.files['upload'].filename
    data = upload_name if upload_name else 'default'
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<img src="' + str(processed) + '">')
