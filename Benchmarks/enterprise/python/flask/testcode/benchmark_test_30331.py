# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest30331():
    upload_name = request.files['upload'].filename
    data = coalesce_blank(upload_name)
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-{}()=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    exec(str(processed))
    return jsonify({"result": "success"})
