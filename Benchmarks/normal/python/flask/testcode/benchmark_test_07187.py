# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
from flask import request, jsonify


def BenchmarkTest07187():
    upload_name = request.files['upload'].filename
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', upload_name):
        return jsonify({'error': 'forbidden'}), 400
    processed = upload_name
    return Markup('<img src="' + str(processed) + '">')
